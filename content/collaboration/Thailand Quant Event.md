---
title: Thailand Quant Events
summary: Thailand Quant Events in 2025–2026
date: 2024-01-01

header:
  caption: ""
  image: ""
---

<style>
  /* Modern table styling */
  .events-wrap { font-size: 16px; }
  .events-header { display:flex; flex-wrap:wrap; gap:12px; align-items:center; margin: 0 0 1rem 0; }
  .events-header h2 { margin: 0; font-size: 1.25rem; }
  .events-search {
    padding: 10px 12px; border: 1px solid var(--card-border-color, #e6e6e6);
    border-radius: 12px; min-width: 260px; flex: 1 1 260px;
  }
  .events-table {
    width: 100%; border-collapse: separate; border-spacing: 0; overflow:hidden;
    border-radius: 14px; box-shadow: 0 6px 24px rgba(0,0,0,.06);
    background: var(--card-bg, #fff);
  }
  .events-table thead th {
    text-align: left; font-weight: 600; letter-spacing: .2px; padding: 14px 16px;
    background: linear-gradient(0deg, rgba(0,0,0,0.02), rgba(0,0,0,0.02));
    border-bottom: 1px solid var(--card-border-color, #eee);
    position: sticky; top: 0; z-index: 1;
  }
  .events-table tbody td { padding: 14px 16px; vertical-align: top; border-bottom: 1px solid #f1f1f1; }
  .events-table tbody tr:hover { background: rgba(0,0,0,0.025); }
  .events-table .title a { text-decoration: none; font-weight: 600; }
  .events-table .badge {
    display:inline-block; padding: 4px 10px; border-radius: 999px; font-size: .85em;
    background: #eef6ff; border: 1px solid #d9ebff;
  }
  .events-year { margin: 2rem 0 1rem; }
  /* Responsive: stack some columns on narrow screens */
  @media (max-width: 800px) {
    .col-summary { display:none; }
    .events-table thead th.summary { display:none; }
  }
</style>

<div class="events-wrap">

  <div class="events-header">
    <h2>Thailand Quant Events (2025–2026)</h2>
    <input class="events-search" id="eventsSearch" type="search" placeholder="Search by title, organizer, location, or year…" />
  </div>

  <!-- 2025 -->
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
      <!-- Replace sample rows with your real events -->
      <tr>
        <td class="title"><a href="#" rel="noopener">Quant Meetup 2025 — Northern Thailand</a></td>
        <td><span class="badge">2025-03-22</span></td>
        <td>Thai Quantitative Analyst & Financial Engineer Association (TQF)</td>
        <td>Chiang Mai</td>
        <td class="col-summary">Community meetup on quantitative finance, alphas, and careers; lightning talks & networking.</td>
        <td><a href="#" rel="noopener">Event page</a></td>
      </tr>
      <tr>
        <td class="title"><a href="#" rel="noopener">AI for Research & Innovation — Hands-on Workshop</a></td>
        <td><span class="badge">2025-05-10</span></td>
        <td>Maejo University · QuantCorner Research Lab</td>
        <td>Chiang Mai / Hybrid</td>
        <td class="col-summary">Practical LLM/agent pipelines for finance and agriculture; notebooks and templates provided.</td>
        <td><a href="#" rel="noopener">Register</a></td>
      </tr>
      <tr>
        <td class="title"><a href="#" rel="noopener">Quantitative Risk Management Mini-Conference</a></td>
        <td><span class="badge">2025-08-16</span></td>
        <td>ResilientML · Partners</td>
        <td>Bangkok</td>
        <td class="col-summary">Talks on copulas, Black-Litterman variants, and stress testing for Thai markets.</td>
        <td><a href="#" rel="noopener">Details</a></td>
      </tr>
    </tbody>
  </table>

  <!-- 2026 -->
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
      <!-- Replace sample rows with your real events -->
      <tr>
        <td class="title"><a href="#" rel="noopener">Thailand Quant Summit 2026</a></td>
        <td><span class="badge">2026-03-07</span></td>
        <td>TQF · Industry Partners</td>
        <td>Bangkok</td>
        <td class="col-summary">Flagship annual summit on quant strategies, infra, and risk with academia–industry panels.</td>
        <td><a href="#" rel="noopener">Event page</a></td>
      </tr>
      <tr>
        <td class="title"><a href="#" rel="noopener">Workshop: Copula-Driven Pair Trading & Hedging</a></td>
        <td><span class="badge">2026-06-20</span></td>
        <td>QuantConnect Research Laboratory</td>
        <td>Bangkok / Online</td>
        <td class="col-summary">From theory to code: HAC/factor copulas for spreads, hedging ratios, and backtests.</td>
        <td><a href="#" rel="noopener">Register</a></td>
      </tr>
      <tr>
        <td class="title"><a href="#" rel="noopener">AI x Agri-Finance Innovation Day</a></td>
        <td><span class="badge">2026-10-03</span></td>
        <td>BAAC Collaborators · QuantCorner</td>
        <td>Bangkok</td>
        <td class="col-summary">Agentic AI dashboards for macro assumptions, green loans, and risk metrics.</td>
        <td><a href="#" rel="noopener">Details</a></td>
      </tr>
    </tbody>
  </table>

</div>

<script>
  // Simple client-side search across both tables
  (function(){
    const input = document.getElementById('eventsSearch');
    const tables = document.querySelectorAll('.events-table tbody');
    function norm(s){ return (s||'').toLowerCase(); }
    input && input.addEventListener('input', function(){
      const q = norm(this.value);
      tables.forEach(tb => {
        Array.from(tb.rows).forEach(tr => {
          const text = norm(tr.innerText);
          tr.style.display = text.includes(q) ? '' : 'none';
        });
      });
    });
  })();
</script>
