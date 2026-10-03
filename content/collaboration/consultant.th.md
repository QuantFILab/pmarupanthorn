---
title: "อุตสาหกรรมและบริษัท"
summary: "อุตสาหกรรม การวิจัย และความร่วมมือทางวิชาชีพ"
date: 2024-01-01

# Optional header image (relative to `assets/media/` folder).
header:
  caption: ""
  image: ""
---

<style>
.industry-collaboration {
  --collab-ink: #10233f;
  --collab-muted: #58677a;
  --collab-line: #d6e2ee;
  --collab-blue: #0969c3;
  --collab-panel: #ffffff;
  --collab-panel-alt: #f6faff;
  --collab-role-bg: #eaf4ff;
  --collab-role-line: #c9e2fb;
  --collab-shadow: 0 10px 28px rgba(15, 47, 82, .08);
  --collab-hover-line: #62a6e4;
  --collab-hover-shadow: 0 16px 38px rgba(15, 108, 189, .16);
  margin: 1.25rem 0 2.5rem;
}

.dark .industry-collaboration {
  --collab-ink: #f4f8fd;
  --collab-muted: #a9b7c9;
  --collab-line: #334963;
  --collab-blue: #72c1ff;
  --collab-panel: #18263b;
  --collab-panel-alt: #121d2f;
  --collab-role-bg: #123353;
  --collab-role-line: #27577f;
  --collab-shadow: 0 12px 30px rgba(0, 0, 0, .28);
  --collab-hover-line: #5eb9ff;
  --collab-hover-shadow: 0 18px 42px rgba(0, 0, 0, .38);
}

.industry-collaboration__intro {
  color: var(--collab-muted);
  font-size: 1.02rem;
  line-height: 1.7;
  margin: 0 0 1.75rem;
  max-width: 780px;
}

.industry-collaboration__section {
  margin-top: 2.25rem;
}

.industry-collaboration__heading {
  align-items: center;
  color: var(--collab-ink);
  display: flex;
  font-size: 1.18rem;
  font-weight: 750;
  gap: .7rem;
  letter-spacing: -.01em;
  margin: 0 0 1rem;
}

.industry-collaboration__heading::after {
  background: linear-gradient(90deg, var(--collab-line), transparent);
  content: "";
  flex: 1;
  height: 1px;
}

.industry-collaboration__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.company-card {
  align-items: center;
  background: linear-gradient(145deg, var(--collab-panel), var(--collab-panel-alt));
  border: 1px solid var(--collab-line);
  border-radius: 16px;
  box-shadow: var(--collab-shadow);
  color: inherit !important;
  display: grid;
  gap: 1rem;
  grid-template-columns: 148px minmax(0, 1fr);
  min-height: 126px;
  overflow: hidden;
  padding: 1rem;
  text-decoration: none !important;
  transition: border-color .18s ease, box-shadow .18s ease, transform .18s ease;
}

.company-card:hover,
.company-card:focus-visible {
  border-color: var(--collab-hover-line);
  box-shadow: var(--collab-hover-shadow);
  outline: none;
  transform: translateY(-2px);
}

.company-card__logo {
  align-items: center;
  background: #ffffff;
  border: 1px solid #edf2f7;
  border-radius: 12px;
  display: flex;
  height: 90px;
  justify-content: center;
  overflow: hidden;
  padding: .75rem;
}

.company-card__logo--dark {
  background: #151a2e;
  border-color: #151a2e;
}

.company-card__logo img {
  display: block;
  max-height: 66px;
  max-width: 100%;
  object-fit: contain;
  width: auto;
}

.company-card__logo--brain img {
  max-height: 52px;
}

.company-card__name {
  color: var(--collab-ink);
  display: block;
  font-size: 1rem;
  font-weight: 750;
  line-height: 1.35;
}

.company-card__role {
  background: var(--collab-role-bg);
  border: 1px solid var(--collab-role-line);
  border-radius: 999px;
  color: var(--collab-blue);
  display: inline-flex;
  font-size: .78rem;
  font-weight: 650;
  margin-top: .45rem;
  padding: .24rem .58rem;
}

.company-card__link {
  color: var(--collab-muted);
  display: block;
  font-size: .78rem;
  margin-top: .4rem;
}

@media (max-width: 820px) {
  .industry-collaboration__grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 520px) {
  .company-card {
    grid-template-columns: 104px minmax(0, 1fr);
    min-height: 112px;
    padding: .8rem;
  }

  .company-card__logo {
    height: 76px;
    padding: .55rem;
  }
}
</style>

<div class="industry-collaboration">
  <p class="industry-collaboration__intro">บทบาทและความร่วมมือทางวิชาชีพที่ครอบคลุมด้านการเงินเชิงปริมาณ วิศวกรรมการเงิน การเรียนรู้ของเครื่อง และการวิจัยในอุตสาหกรรม.</p>

  <section class="industry-collaboration__section" aria-labelledby="committee-heading">
    <h2 class="industry-collaboration__heading" id="committee-heading">คณะกรรมการ</h2>
    <div class="industry-collaboration__grid">
      <a class="company-card" href="https://www.tqf.or.th/" target="_blank" rel="noopener noreferrer">
        <span class="company-card__logo">
          <img src="../../media/collaboration/tqf.png" alt="Thai Association of Quantitative Analysts and Financial Engineers logo" loading="lazy">
        </span>
        <span>
          <span class="company-card__name">สมาคมนักวิเคราะห์เชิงปริมาณและวิศวกรการเงินแห่งประเทศไทย</span>
          <span class="company-card__role">รองประธาน</span>
          <span class="company-card__link">เยี่ยมชมองค์กร ↗</span>
        </span>
      </a>
    </div>
  </section>
  <section class="industry-collaboration__section" aria-labelledby="collaborations-heading">
    <h2 class="industry-collaboration__heading" id="collaborations-heading">งานและความร่วมมือ</h2>
    <div class="industry-collaboration__grid">
      <a class="company-card" href="https://www.resilientml.com/" target="_blank" rel="noopener noreferrer">
        <span class="company-card__logo">
          <img src="../../media/collaboration/resilientml.png" alt="ResilientML logo" loading="lazy">
        </span>
        <span>
          <span class="company-card__name">ResilientML</span>
          <span class="company-card__role">นักวิจัยเชิงปริมาณ</span>
          <span class="company-card__link">เยี่ยมชมบริษัท ↗</span>
        </span>
      </a>
      <a class="company-card" href="https://www.quant-corner.com/about-3" target="_blank" rel="noopener noreferrer">
        <span class="company-card__logo company-card__logo--dark">
          <img src="../../media/collaboration/quantcorner.svg" alt="QuantCorner Research Laboratory logo" loading="lazy">
        </span>
        <span>
          <span class="company-card__name">ห้องปฏิบัติการวิจัย QuantCorner</span>
          <span class="company-card__role">ผู้อำนวยการ</span>
          <span class="company-card__link">เยี่ยมชมห้องปฏิบัติการวิจัย ↗</span>
        </span>
      </a>
      <a class="company-card" href="https://groundup.in.th/" target="_blank" rel="noopener noreferrer">
        <span class="company-card__logo">
          <img src="../../media/collaboration/groundup-academy.webp" alt="GroundUp Academy logo" loading="lazy">
        </span>
        <span>
          <span class="company-card__name">GroundUp Academy</span>
          <span class="company-card__role">ผู้ร่วมก่อตั้ง</span>          <span class="company-card__link">เยี่ยมชมสถาบัน ↗</span>
        </span>
      </a>
    </div>
  </section>

  <section class="industry-collaboration__section" aria-labelledby="consultant-heading">
    <h2 class="industry-collaboration__heading" id="consultant-heading">ที่ปรึกษา</h2>
    <div class="industry-collaboration__grid">
      <a class="company-card" href="https://www.worldquant.com/brain/" target="_blank" rel="noopener noreferrer">
        <span class="company-card__logo company-card__logo--dark company-card__logo--brain">
          <img src="../../media/collaboration/worldquant-brain.svg" alt="WorldQuant BRAIN logo" loading="lazy">
        </span>
        <span>
          <span class="company-card__name">WorldQuant BRAIN</span>
          <span class="company-card__role">ที่ปรึกษาด้านการวิจัย</span>
          <span class="company-card__link">เยี่ยมชม WorldQuant BRAIN ↗</span>
        </span>
      </a>
    </div>
  </section>
</div>
