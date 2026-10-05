---
title: ""
date: 2022-10-24
type: landing

design:
  spacing: "6rem"

sections:
  - block: resume-biography-3
    content:
      username: admin
      text: ""
      button:
        text: Download CV
        url: uploads/resume.pdf
    design:
      columns: '1'
  - block: markdown
    id: communication
    content:
      title: Communication
      text: |
        <div class="communication-table-wrap">
          <table class="communication-table">
            <thead>
              <tr>
                <th scope="col">Date</th>
                <th scope="col">Type</th>
                <th scope="col">Announcement</th>
                <th scope="col">More</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><time datetime="2026-09-12">12 Sep 2026</time></td>
                <td><span class="communication-tag" data-kind="research">Research</span></td>
                <td>I'm delighted to share that our paper, <strong>“State Conditional Boosting for Prospective Early Warning of CFPB Reported Relief Workload,”</strong> has been published in <em>Operations Research Forum</em>. The research develops an explainable prospective early-warning framework for prioritising company–product cells with increasing CFPB-reported relief workload.</td>
                <td><a href="/pmarupanthorn/publication/orf2026/">Read the research summary <span aria-hidden="true">→</span></a></td>
              </tr>
              <tr>
                <td><time datetime="2026-09-13">13 Sep 2026</time></td>
                <td><span class="communication-tag" data-kind="research">Research</span></td>
                <td>I'm delighted to share that our paper, <strong>“Policy-state gated regime dynamics in European emission allowance futures,”</strong> has been published in <em>Discover Sustainability</em>. The study introduces a policy-state-gated regime model for interpreting low- and high-volatility conditions in European carbon-allowance futures.</td>
                <td><a href="/pmarupanthorn/publication/ds2026/">Read the research summary <span aria-hidden="true">→</span></a></td>
              </tr>
              <tr>
                <td><time datetime="2026-11-21">21 Nov 2026</time></td>
                <td><span class="communication-tag" data-kind="talk">Talk</span><span class="communication-tag" data-kind="trading">Trading</span></td>
                <td>I'm pleased to announce that I will present <strong>“Statistical Arbitrage in Derivative Market”</strong> at CAF Seminar 2026, hosted at the Stock Exchange of Thailand on 21 November 2026. The session will connect statistical-arbitrage methods with systematic trading in derivative markets.</td>
                <td><a href="/pmarupanthorn/event/cafstatarb2026/">View talk details <span aria-hidden="true">→</span></a></td>
              </tr>
              <tr>
                <td><time datetime="2026-10-10">10 Oct 2026</time></td>
                <td><span class="communication-tag" data-kind="talk">Talk</span></td>
                <td>I'm honoured to deliver the keynote lecture <strong>“Quantitative Finance in the Age of Digital Innovation”</strong> at the DIFT 2026-2 Conference on 10 October 2026. The lecture will introduce how quantitative finance, data-driven research, and systematic methods connect with digital innovation and financial technology.</td>
                <td><a href="/pmarupanthorn/event/dift2026-2/">View keynote details <span aria-hidden="true">→</span></a></td>
              </tr>
              <tr>
                <td><time datetime="2026-09-30">30 Sep 2026</time></td>
                <td><span class="communication-tag" data-kind="talk">Talk</span><span class="communication-tag" data-kind="trading">Trading</span></td>
                <td>I recently delivered <strong>“Quant Career: Financial Engineer,”</strong> a free Groundup Academy session introducing the responsibilities, technical skills, and financial-modelling knowledge required for careers in equity and commodity derivatives.</td>
                <td><a href="/pmarupanthorn/event/quantcareer2026/">View session summary <span aria-hidden="true">→</span></a></td>
              </tr>
            </tbody>
          </table>
          <nav class="communication-pagination" aria-label="Communication pages" hidden>
            <a class="communication-page-prev" href="#communication">← Previous</a>
            <span class="communication-page-status" aria-live="polite"></span>
            <a class="communication-page-next" href="#communication">Next →</a>
          </nav>
        </div>
    design:
      spacing:
        padding: ["3rem", "0", "3rem", "0"]
  - block: collection
    id: papers
    content:
      title: Featured Publications
      count: 0
      filters:
        folders:
          - publication
        featured_only: true
    design:
      view: article-grid
      columns: 4
  - block: collection
    content:
      title: Recent Publications
      count: 3
      text: ""
      filters:
        folders:
          - publication
        exclude_featured: false
    design:
      view: citation
  - block: collection
    id: talks
    content:
      title: Recent & Upcoming Talks
      count: 3
      filters:
        folders:
          - event
    design:
      view: article-grid
      columns: 3
      fill_image: false
  - block: collection
    id: courses
    content:
      title: Featured Courses
      count: 3
      filters:
        folders:
          - teaching
    design:
      view: article-grid
      columns: 3
      fill_image: false
  - block: markdown
    id: leadership
    content:
      title: Professional Leadership & Impact
      text: |
        - **Vice President**, [Thailand Association of Quantitative Analysts and Financial Engineers (TQF)](https://www.tqf.or.th/team)
        - **Director**, [QuantCorner Research Laboratory](https://www.quant-corner.com/about-3)
        - **Co-Founder / Quantitative Researcher / Trader**, L2 Technology
        - **Co-Founder / Researcher / Lecturer**, Groundup Academy
        - **WorldQuant BRAIN Gold Level**, [Certificate of Accomplishment](/pmarupanthorn/uploads/worldquant-brain-gold-certificate.png)

        **Current site portfolio:** 19 publications and working papers · 46 talks and workshops · 10 courses · 11 research themes
  - block: markdown
    id: collaboration
    content:
      title: Work With Me
      text: |
        I welcome collaborations with researchers, universities, financial institutions, insurers, technology teams, and professional communities.

        - **Research collaboration** in quantitative finance, insurance, carbon markets, statistical arbitrage, and statistical machine learning
        - **Invited talks and workshops** for academic and professional audiences
        - **Industry research and training** in quantitative investment, derivatives, risk analytics, and AI
        - **Student supervision** for aligned doctoral, master's, and undergraduate projects

        [Email me](mailto:quantfilab@gmail.com) · [LinkedIn](https://uk.linkedin.com/in/pasin-marupanthorn) · [Collaboration and supervision](/pmarupanthorn/collaboration/)
---
