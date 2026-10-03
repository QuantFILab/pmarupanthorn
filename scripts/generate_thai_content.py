"""Generate native Thai Hugo page translations from the English content tree.

The generator preserves code, mathematical expressions, Hugo shortcodes, scripts,
styles, URLs, and media references. Existing curated bilingual publication and
policy shortcodes remain the source of truth for those page bodies.
"""

from __future__ import annotations

import hashlib
import http.cookiejar
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
CACHE_PATH = ROOT / "tmp" / "thai-translation-cache-bing.json"
TRANSLATOR_PAGE = "https://www.bing.com/translator"
TRANSLATE_ENDPOINT = "https://www.bing.com/ttranslatev3"
MAX_CHUNK = 900
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)

TRANSLATABLE_KEYS = {
    "title",
    "summary",
    "text",
    "caption",
    "role",
    "description",
    "area",
    "position",
    "company_name",
}

CURATED = {
    "Pasin Marupanthorn": "พศิน มรุปัณฑ์ธร",
    "Books": "หนังสือ",
    "Book Series": "ชุดหนังสือ",
    "Courses": "รายวิชา",
    "Research Themes": "หัวข้องานวิจัย",
    "Policy/Industry Support": "การสนับสนุนนโยบายและภาคอุตสาหกรรม",
    "Publications": "ผลงานตีพิมพ์",
    "Experience": "ประสบการณ์",
    "Collaboration": "ความร่วมมือ",
    "Industry and Company": "อุตสาหกรรมและบริษัท",
    "Personal Collaboration": "ความร่วมมือส่วนบุคคล",
    "Student Supervision & Opportunities": "การดูแลนักศึกษาและโอกาสทางการศึกษา",
    "Thailand Quant Events": "กิจกรรมควอนต์ในประเทศไทย",
    "Projects": "โครงการ",
    "Trading Record": "ประวัติการซื้อขาย",
}


def load_curated_research_titles() -> dict[str, str]:
    data_path = ROOT / "data" / "research_overviews.yaml"
    if not data_path.exists():
        return {}
    titles: dict[str, str] = {}
    current_key = ""
    in_thai = False
    for line in data_path.read_text(encoding="utf-8-sig").splitlines():
        top_key = re.match(r"^([A-Za-z0-9_-]+):\s*$", line)
        if top_key:
            current_key = top_key.group(1)
            in_thai = False
            continue
        if line == "  th:":
            in_thai = True
            continue
        if in_thai and current_key:
            title_match = re.match(r'^    title:\s*["\'](.*)["\']\s*$', line)
            if title_match:
                titles[current_key] = title_match.group(1)
                in_thai = False
    return titles


RESEARCH_TITLES = load_curated_research_titles()

PROTECTED_PATTERNS = [
    re.compile(r"```.*?```", re.DOTALL),
    re.compile(r"~~~.*?~~~", re.DOTALL),
    re.compile(r"<style\b.*?</style>", re.DOTALL | re.IGNORECASE),
    re.compile(r"<script\b.*?</script>", re.DOTALL | re.IGNORECASE),
    re.compile(r"\{\{[<%].*?[>%]\}\}", re.DOTALL),
    re.compile(r"\{\{.*?\}\}", re.DOTALL),
    re.compile(r"\$\$.*?\$\$", re.DOTALL),
    re.compile(r"\\\[.*?\\\]", re.DOTALL),
    re.compile(r"\\\(.*?\\\)", re.DOTALL),
    re.compile(r"`[^`\n]+`"),
    re.compile(r"</?[A-Za-z][^>\n]*>"),
    re.compile(r"(?:https?://|mailto:)[^\s)\]>\"']+", re.IGNORECASE),
    re.compile(r"(?<![\w.])/(?:[\w.-]+/)*[\w.%-]+/?"),
]

COOKIE_JAR = http.cookiejar.CookieJar()
OPENER = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(COOKIE_JAR))
BING_CREDENTIALS: dict[str, str] = {}


def load_cache() -> dict[str, str]:
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


CACHE = load_cache()


def save_cache() -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(
        json.dumps(CACHE, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def refresh_bing_credentials() -> None:
    request = urllib.request.Request(TRANSLATOR_PAGE, headers={"User-Agent": USER_AGENT})
    with OPENER.open(request, timeout=45) as response:
        page = response.read().decode("utf-8", errors="replace")

    token_match = re.search(
        r'params_AbusePreventionHelper\s*=\s*\[(\d+),"([^"]+)",', page
    )
    ig_matches = re.findall(r'(?i)["\']ig["\']\s*:\s*["\']([A-F0-9]{32})["\']', page)
    iid_matches = re.findall(r'data-iid="([^"]+)"', page)
    if not token_match or not ig_matches or not iid_matches:
        raise RuntimeError("Could not read Bing Translator session credentials")

    BING_CREDENTIALS.update(
        {
            "key": token_match.group(1),
            "token": token_match.group(2),
            "ig": ig_matches[-1],
            "iid": iid_matches[-1],
        }
    )


def needs_translation(text: str) -> bool:
    return bool(re.search(r"[A-Za-z]", text)) and not re.search(r"[ก-๙]", text)


def translate_request(text: str) -> str:
    normalized = text.strip()
    if not normalized or not needs_translation(normalized):
        return text
    if normalized in CURATED:
        replacement = CURATED[normalized]
        return text.replace(normalized, replacement, 1)

    cache_key = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if cache_key in CACHE:
        return CACHE[cache_key]

    last_error: Exception | None = None
    for attempt in range(5):
        try:
            if not BING_CREDENTIALS or attempt:
                refresh_bing_credentials()
            query = urllib.parse.urlencode(
                {
                    "isVertical": "1",
                    "IG": BING_CREDENTIALS["ig"],
                    "IID": BING_CREDENTIALS["iid"],
                }
            )
            body = urllib.parse.urlencode(
                {
                    "fromLang": "en",
                    "to": "th",
                    "text": text,
                    "token": BING_CREDENTIALS["token"],
                    "key": BING_CREDENTIALS["key"],
                }
            ).encode("utf-8")
            request = urllib.request.Request(
                f"{TRANSLATE_ENDPOINT}?{query}",
                data=body,
                headers={
                    "User-Agent": USER_AGENT,
                    "Origin": "https://www.bing.com",
                    "Referer": TRANSLATOR_PAGE,
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            )
            with OPENER.open(request, timeout=45) as response:
                payload = json.loads(response.read().decode("utf-8"))
            translated = payload[0]["translations"][0]["text"]
            CACHE[cache_key] = translated
            save_cache()
            time.sleep(0.12)
            return translated
        except Exception as error:  # Network errors are retried with backoff.
            last_error = error
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Translation request failed: {last_error}")


def protect_text(text: str) -> tuple[str, dict[str, str]]:
    protected: dict[str, str] = {}

    def replace(match: re.Match[str]) -> str:
        token = f"ZXQ{len(protected):05d}QXZ"
        protected[token] = match.group(0)
        return token

    result = text
    for pattern in PROTECTED_PATTERNS:
        result = pattern.sub(replace, result)
    return result, protected


def restore_text(text: str, protected: dict[str, str]) -> str:
    result = text
    for token, original in protected.items():
        result = result.replace(token, original)
    # Machine translation can add harmless spaces around Markdown delimiters.
    result = re.sub(r"\*\*\s+([^*\n]+?)\s+\*\*", r"**\1**", result)
    result = re.sub(r"\[\s*([^\]\n]+?)\s*\]\(\s*([^\)\n]+?)\s*\)", r"[\1](\2)", result)
    return result


def split_chunks(text: str) -> list[str]:
    if len(text) <= MAX_CHUNK:
        return [text]

    pieces = re.split(r"(\n{2,})", text)
    chunks: list[str] = []
    current = ""
    for piece in pieces:
        if len(current) + len(piece) <= MAX_CHUNK:
            current += piece
            continue
        if current:
            chunks.append(current)
            current = ""
        if len(piece) <= MAX_CHUNK:
            current = piece
            continue
        lines = piece.splitlines(keepends=True)
        for line in lines:
            if len(current) + len(line) > MAX_CHUNK and current:
                chunks.append(current)
                current = ""
            if len(line) > MAX_CHUNK:
                for start in range(0, len(line), MAX_CHUNK):
                    part = line[start : start + MAX_CHUNK]
                    if current:
                        chunks.append(current)
                        current = ""
                    chunks.append(part)
            else:
                current += line
    if current:
        chunks.append(current)
    return chunks


def translate_long(text: str) -> str:
    protected_text, protected = protect_text(text)
    translated = "".join(translate_request(chunk) for chunk in split_chunks(protected_text))
    return restore_text(translated, protected)


def yaml_scalar(value: str) -> str:
    stripped = value.strip()
    if len(stripped) >= 2 and stripped[0] == stripped[-1] and stripped[0] in "\"'":
        return stripped[1:-1]
    return stripped


def translate_frontmatter(frontmatter: str) -> str:
    lines = frontmatter.splitlines()
    top_level_overrides: dict[str, str] = {}
    for line in lines:
        match = re.match(r"^(title_th|summary_th):\s*(.+?)\s*$", line)
        if match:
            top_level_overrides[match.group(1).removesuffix("_th")] = yaml_scalar(
                match.group(2)
            )

    output: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        match = re.match(
            r"^(?P<indent>\s*)(?P<key>[A-Za-z_][\w-]*):(?P<space>\s*)(?P<value>.*)$",
            line,
        )
        if not match or match.group("key") not in TRANSLATABLE_KEYS:
            output.append(line)
            index += 1
            continue

        indent = match.group("indent")
        key = match.group("key")
        value = match.group("value").strip()
        override = top_level_overrides.get(key) if not indent else None

        if value in {"|", "|-", ">", ">-"}:
            block: list[str] = []
            cursor = index + 1
            while cursor < len(lines):
                next_line = lines[cursor]
                if next_line.strip() and len(next_line) - len(next_line.lstrip()) <= len(indent):
                    break
                block.append(next_line)
                cursor += 1
            if override:
                output.append(f"{indent}{key}: {json.dumps(override, ensure_ascii=False)}")
            else:
                output.append(line)
                if block:
                    nonempty = [item for item in block if item.strip()]
                    base_indent = min(
                        (len(item) - len(item.lstrip()) for item in nonempty),
                        default=len(indent) + 2,
                    )
                    raw_block = "\n".join(item[base_indent:] for item in block)
                    translated = translate_long(raw_block)
                    output.extend(
                        (" " * base_indent + item if item else "")
                        for item in translated.splitlines()
                    )
            index = cursor
            continue

        if not value or value in {"''", '""'}:
            output.append(line)
            index += 1
            continue

        plain = override or yaml_scalar(value)
        if (
            plain.startswith(("http://", "https://", "/"))
            or re.fullmatch(r"(?:true|false|null|\d+(?:\.\d+)?)", plain, re.IGNORECASE)
            or not needs_translation(plain)
        ):
            translated = plain
        else:
            translated = translate_long(plain)
        output.append(f"{indent}{key}: {json.dumps(translated, ensure_ascii=False)}")
        index += 1

    return "\n".join(output)


def split_document(source: str) -> tuple[str, str]:
    if not source.startswith("---"):
        return "", source
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", source, re.DOTALL)
    if not match:
        return "", source
    return match.group(1), source[match.end() :]


def thai_destination(source: Path) -> Path:
    return source.with_name(f"{source.stem}.th{source.suffix}")


def generate_page(source_path: Path) -> Path:
    source = source_path.read_text(encoding="utf-8-sig")
    frontmatter, body = split_document(source)
    translated_frontmatter = translate_frontmatter(frontmatter) if frontmatter else ""

    has_curated_body = "{{< research-bilingual" in body or "{{< policy-bilingual" in body
    research_key_match = re.search(r'\{\{<\s*research-bilingual\s+key="([^"]+)"', body)
    if research_key_match and research_key_match.group(1) in RESEARCH_TITLES:
        curated_title = json.dumps(
            RESEARCH_TITLES[research_key_match.group(1)], ensure_ascii=False
        )
        translated_frontmatter = re.sub(
            r"(?m)^title:\s*.*$", f"title: {curated_title}", translated_frontmatter, count=1
        )
    translated_body = body if has_curated_body else translate_long(body)

    if translated_frontmatter:
        result = f"---\n{translated_frontmatter}\n---\n\n{translated_body.lstrip()}"
    else:
        result = translated_body
    if not result.endswith("\n"):
        result += "\n"

    destination = thai_destination(source_path)
    destination.write_text(result, encoding="utf-8", newline="\n")
    return destination


def main() -> None:
    sources = sorted(
        path
        for path in CONTENT.rglob("*.md")
        if not path.name.endswith(".th.md")
    )
    for number, source in enumerate(sources, start=1):
        destination = generate_page(source)
        print(f"[{number:03d}/{len(sources):03d}] {destination.relative_to(ROOT)}")
    save_cache()
    print(f"Generated {len(sources)} Thai content files.")


if __name__ == "__main__":
    main()
