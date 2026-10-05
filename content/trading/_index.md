---
title: Trading
type: landing
cascade:
  - _target:
      kind: page
    params:
      show_breadcrumb: true
sections:
  - block: markdown
    id: quant-practice
    content:
      title: Quant Practice
      text: |
        <section class="quant-practice-tier" aria-labelledby="alpha-research-tier">
          <header class="quant-practice-tier__header">
            <span class="quant-practice-tier__label">Tier 01</span>
            <div>
              <h3 id="alpha-research-tier">Alpha Research</h3>
              <p>External quantitative-research platforms for developing and testing predictive signals.</p>
              <p class="quant-practice-tier__path"><span>Alpha</span><span aria-hidden="true">→</span><span>Money</span></p>
            </div>
          </header>

          <div class="quant-practice-table-wrap">
            <table class="quant-practice-table">
              <thead>
                <tr>
                  <th scope="col">Platform / Programme</th>
                  <th scope="col">Practice focus</th>
                  <th scope="col">Page</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row"><a href="/pmarupanthorn/trading/worldquant-brain-alpha-research/">WorldQuant BRAIN Alpha Research</a></th>
                  <td>Quantitative alpha research and model development.</td>
                  <td><a class="quant-practice-table__link" href="/pmarupanthorn/trading/worldquant-brain-alpha-research/">Introduction <span aria-hidden="true">→</span></a></td>
                </tr>
                <tr>
                  <th scope="row"><a href="/pmarupanthorn/trading/trexquant-global-alpha-researcher/">Trexquant Global Alpha Researcher (GAR)</a></th>
                  <td>Contract-based global alpha research, simulation, and strategy development.</td>
                  <td><a class="quant-practice-table__link" href="/pmarupanthorn/trading/trexquant-global-alpha-researcher/">Introduction <span aria-hidden="true">→</span></a></td>
                </tr>
                <tr>
                  <th scope="row"><a href="https://quantiacs.com/" target="_blank" rel="noopener">Quantiacs</a></th>
                  <td>A strong alternative for developing complete portfolio algorithms.</td>
                  <td><a class="quant-practice-table__link" href="https://quantiacs.com/" target="_blank" rel="noopener">Official platform <span aria-hidden="true">↗</span></a></td>
                </tr>
                <tr>
                  <th scope="row"><a href="https://signals.numer.ai/" target="_blank" rel="noopener">Numerai Signals</a></th>
                  <td>Best suited when the intellectual asset is your own data or factor model.</td>
                  <td><a class="quant-practice-table__link" href="https://signals.numer.ai/" target="_blank" rel="noopener">Official platform <span aria-hidden="true">↗</span></a></td>
                </tr>
                <tr>
                  <th scope="row"><a href="https://docs.crunchdao.com/competitions/competitions/datacrunch-competition" target="_blank" rel="noopener">CrunchDAO / DataCrunch</a></th>
                  <td>Advanced research competitions with live financial relevance to alpha.</td>
                  <td><a class="quant-practice-table__link" href="https://docs.crunchdao.com/competitions/competitions/datacrunch-competition" target="_blank" rel="noopener">Official platform <span aria-hidden="true">↗</span></a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
    design:
      spacing:
        padding: ["4.5rem", "0", "3rem", "0"]
  - block: markdown
    id: trading-achievement
    content:
      title: My Achievement
      text: |
        <div class="trading-achievement-grid">
          <article class="trading-achievement-card">
            <a class="trading-achievement-card__media trading-achievement-card__media--certificate" href="/pmarupanthorn/uploads/worldquant-brain-gold-certificate.png" target="_blank" rel="noopener">
              <img src="/pmarupanthorn/uploads/worldquant-brain-gold-certificate.png" alt="WorldQuant BRAIN Gold Level Certificate of Accomplishment" loading="lazy">
            </a>
            <div class="trading-achievement-card__body">
              <span class="trading-achievement-card__eyebrow">WorldQuant BRAIN</span>
              <h3>Gold Medal Achievement</h3>
              <p>Certificate of Accomplishment for reaching Gold Level in the WorldQuant Challenge.</p>
              <a class="trading-achievement-card__link" href="/pmarupanthorn/uploads/worldquant-brain-gold-certificate.png" target="_blank" rel="noopener">View certificate <span aria-hidden="true">↗</span></a>
            </div>
          </article>

          <article class="trading-achievement-card trading-achievement-card--performance">
            <div class="trading-achievement-card__media trading-achievement-card__media--performance">
              <a href="/pmarupanthorn/uploads/trading-return-10-percent-2026.png" target="_blank" rel="noopener">
                <img src="/pmarupanthorn/uploads/trading-return-10-percent-2026.png" alt="Trading performance chart showing the return reaching 10 percent" loading="lazy">
              </a>
              <a href="/pmarupanthorn/uploads/trading-performance-statistics-2026.png" target="_blank" rel="noopener">
                <img src="/pmarupanthorn/uploads/trading-performance-statistics-2026.png" alt="Trading performance statistics showing 11.55 percent cumulative return and a Sharpe ratio of 6.79" loading="lazy">
              </a>
            </div>
            <div class="trading-achievement-card__body">
              <span class="trading-achievement-card__eyebrow">Statistical Arbitrage · U.S. Equities</span>
              <h3>10% Return Milestone with a High Sharpe Ratio</h3>
              <p>A statistical arbitrage trading strategy applied to the U.S. equity market.</p>
              <div class="trading-achievement-metrics" aria-label="Trading performance highlights">
                <span><strong>11.55%</strong>Cumulative return</span>
                <span><strong>6.79</strong>Sharpe ratio</span>
                <span><strong>0.00%</strong>Maximum drawdown</span>
              </div>
            </div>
          </article>
        </div>
    design:
      spacing:
        padding: ["4rem", "0", "4rem", "0"]
  - block: collection
    id: trading-record
    content:
      title: Trading Record
      count: 10
      filters:
        folders:
          - trading
        tag: live
    design:
      view: article-grid
      columns: 2
      fill_image: false
---
