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
        <div class="trading-practice-grid">
          <article class="trading-practice-card">
            <div class="trading-practice-card__media">
              <span class="trading-practice-card__index">01</span>
              <span class="trading-practice-card__symbol" aria-hidden="true">α</span>
            </div>
            <div class="trading-practice-card__body">
              <h3><a href="/pmarupanthorn/trading/worldquant-brain-alpha-research/">WorldQuant BRAIN Alpha Research</a></h3>
              <p>Quantitative alpha research and model development.</p>
              <a class="trading-practice-card__link" href="/pmarupanthorn/trading/worldquant-brain-alpha-research/">Read the introduction <span aria-hidden="true">→</span></a>
            </div>
          </article>

          <article class="trading-practice-card trading-practice-card--placeholder">
            <div class="trading-practice-card__media">
              <span class="trading-practice-card__index">02</span>
              <span class="trading-practice-card__symbol" aria-hidden="true">＋</span>
            </div>
            <div class="trading-practice-card__body">
              <h3>Other Quant Practice</h3>
              <p>Additional practice details will be added here.</p>
            </div>
          </article>
        </div>
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
