---
title: Thailand Quant Events
summary: Thailand Quant Events in 2025–2026
date: 2024-01-01

header:
  caption: ""
  image: ""
---

<style>
  .events-wrap { font-size: 16px; }
  .events-header { display:flex; flex-wrap:wrap; gap:12px; align-items:center; margin-bottom:1rem; }
  .events-search {
    padding:10px 12px; border:1px solid #ddd; border-radius:12px; min-width:260px;
  }
  .events-table {
    width:100%; border-collapse:separate; border-spacing:0; overflow:hidden;
    border-radius:14px; box-shadow:0 6px 24px rgba(0,0,0,.06); background:#fff;
  }
  .events-table th, .events-table td {
    padding:14px 16px; text-align:left; border-bottom:1px solid #f1f1f1;
  }
  .events-table th { background:#fafafa; font-weight:600; }
  .events-table tr:hover { background:rgba(0,0,0,0.025); }
  .events-table .badge {
    display:inline-block; padding:4px 10px; border-radius:999px;
    background:#eef6ff; border:1px solid #d9ebff; font-size:0.85em;
  }
  @media (max-width:800px) {
    .col-summary, th.summary { display:none; }
  }
</style>

<div class="events-wrap">
  <div class="events-header">
    <h2>Thailand Quant Events (2025–2026)</h2>
    <input class="events-search" id="eventsSearch" type="search" placeholder="Search by title, organizer, or location…" />
  </div>
  
  <h3 class="events-year">2025</h3>
  <table class="events-table" data-year="2025">
    <thead>
      <tr>
        <th class="title">Title of event</th>
        <th>Date</th>
        <th>Organizer</th>
        <th>Location</th>
        <th class="summary">Summary</th>
        <th>Link</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="title">Workshop: Copula-Driven Pair Trading &amp; Hedging</td>
        <td><span class="badge">2025-05-10</span></td>
        <td>Maejo University · QuantCorner Research Lab</td>
        <td>Chiang Mai / Hybrid</td>
        <td class="col-summary">Practical LLM/agent pipelines for finance and agriculture; notebooks and templates provided.</td>
        <td></td>
      </tr>
    </tbody>
  </table>
  
  <h3 class="events-year">2026</h3>
  <table class="events-table" data-year="2026">
    <thead>
      <tr>
        <th class="title">Title of event</th>
        <th>Date</th>
        <th>Organizer</th>
        <th>Location</th>
        <th class="summary">Summary</th>
        <th>Link</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="title"><a href="https://quantfilab.github.io/pmarupanthorn/collaboration/thailand-quant-event/#" rel="noopener">Quant Meetup 2025 — Northern Thailand</a></td>
        <td><span class="badge">2026-03-07</span></td>
        <td>TQF · Industry Partners</td>
        <td>Bangkok</td>
        <td class="col-summary">Flagship annual summit on quant strategies, infra, and risk with academia–industry panels.</td>
        <td><a href="https://quantfilab.github.io/pmarupanthorn/collaboration/thailand-quant-event/#" rel="noopener">Event page</a></td>
      </tr>
    </tbody>
  </table>
</div>

<script>
(function(){
  const input=document.getElementById('eventsSearch');
  const tables=document.querySelectorAll('.events-table tbody');
  function norm(s){return (s||'').toLowerCase();}
  input.addEventListener('input',function(){
    const q=norm(this.value);
    tables.forEach(tb=>{
      Array.from(tb.rows).forEach(tr=>{
        const text=norm(tr.innerText);
        tr.style.display=text.includes(q)?'':'none';
      });
    });
  });
})();
</script>
