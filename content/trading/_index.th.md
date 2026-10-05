---
title: "การซื้อขาย"
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
      title: "การฝึกปฏิบัติเชิงปริมาณ"
      text: |
        <div class="trading-practice-grid">
          <article class="trading-practice-card">
            <div class="trading-practice-card__media">
              <span class="trading-practice-card__index">01</span>
              <span class="trading-practice-card__symbol" aria-hidden="true">α</span>
            </div>
            <div class="trading-practice-card__body">
              <h3><a href="/pmarupanthorn/th/trading/worldquant-brain-alpha-research/">การวิจัยอัลฟาบน WorldQuant BRAIN</a></h3>
              <p>การวิจัยอัลฟาเชิงปริมาณและการพัฒนาแบบจำลอง</p>
              <a class="trading-practice-card__link" href="/pmarupanthorn/th/trading/worldquant-brain-alpha-research/">อ่านบทนำ <span aria-hidden="true">→</span></a>
            </div>
          </article>

          <article class="trading-practice-card trading-practice-card--placeholder">
            <div class="trading-practice-card__media">
              <span class="trading-practice-card__index">02</span>
              <span class="trading-practice-card__symbol" aria-hidden="true">＋</span>
            </div>
            <div class="trading-practice-card__body">
              <h3>การฝึกปฏิบัติด้านควอนต์อื่น ๆ</h3>
              <p>รายละเอียดเพิ่มเติมจะเพิ่มในภายหลัง</p>
            </div>
          </article>
        </div>
    design:
      spacing:
        padding: ["4.5rem", "0", "3rem", "0"]
  - block: markdown
    id: trading-achievement
    content:
      title: "ความสำเร็จของผม"
      text: |
        <div class="trading-achievement-grid">
          <article class="trading-achievement-card">
            <a class="trading-achievement-card__media trading-achievement-card__media--certificate" href="/pmarupanthorn/uploads/worldquant-brain-gold-certificate.png" target="_blank" rel="noopener">
              <img src="/pmarupanthorn/uploads/worldquant-brain-gold-certificate.png" alt="ใบรับรองความสำเร็จระดับทอง WorldQuant BRAIN" loading="lazy">
            </a>
            <div class="trading-achievement-card__body">
              <span class="trading-achievement-card__eyebrow">WorldQuant BRAIN</span>
              <h3>ความสำเร็จระดับเหรียญทอง</h3>
              <p>ใบรับรองความสำเร็จจากการบรรลุระดับทองในการแข่งขัน WorldQuant Challenge</p>
              <a class="trading-achievement-card__link" href="/pmarupanthorn/uploads/worldquant-brain-gold-certificate.png" target="_blank" rel="noopener">ดูใบรับรอง <span aria-hidden="true">↗</span></a>
            </div>
          </article>

          <article class="trading-achievement-card trading-achievement-card--performance">
            <div class="trading-achievement-card__media trading-achievement-card__media--performance">
              <a href="/pmarupanthorn/uploads/trading-return-10-percent-2026.png" target="_blank" rel="noopener">
                <img src="/pmarupanthorn/uploads/trading-return-10-percent-2026.png" alt="กราฟผลการซื้อขายแสดงผลตอบแทนแตะระดับ 10 เปอร์เซ็นต์" loading="lazy">
              </a>
              <a href="/pmarupanthorn/uploads/trading-performance-statistics-2026.png" target="_blank" rel="noopener">
                <img src="/pmarupanthorn/uploads/trading-performance-statistics-2026.png" alt="สถิติการซื้อขายแสดงผลตอบแทนสะสม 11.55 เปอร์เซ็นต์และอัตราส่วนชาร์ป 6.79" loading="lazy">
              </a>
            </div>
            <div class="trading-achievement-card__body">
              <span class="trading-achievement-card__eyebrow">Statistical Arbitrage · หุ้นสหรัฐฯ</span>
              <h3>ผลตอบแทนแตะ 10% พร้อมอัตราส่วนชาร์ปในระดับสูง</h3>
              <p>กลยุทธ์การซื้อขายแบบ Statistical Arbitrage ที่ใช้กับตลาดหุ้นสหรัฐฯ</p>
              <div class="trading-achievement-metrics" aria-label="ข้อมูลสำคัญของผลการซื้อขาย">
                <span><strong>11.55%</strong>ผลตอบแทนสะสม</span>
                <span><strong>6.79</strong>อัตราส่วนชาร์ป</span>
                <span><strong>0.00%</strong>การขาดทุนสูงสุด</span>
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
      title: "ประวัติการซื้อขาย"
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
