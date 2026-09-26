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
      css_class: dark
      background:
        color: black
      columns: '1'
  - block: markdown
    id: current-research
    content:
      title: Current Research 2026–2031
      text: |
        - **[Carbon Markets](/pmarupanthorn/research/carbon-market/)** — emissions trading systems, carbon credits, policy regimes, and market risk.
        - **[Statistical Arbitrage](/pmarupanthorn/tags/statistical-arbitrage/)** — pairs trading, derivatives, market microstructure, and systematic strategy design.
        - **[Insurance-linked Investment](/pmarupanthorn/research/insurance-market/)** — actuarial pricing, insurance risk, and investment-linked insurance applications.
        - **[Statistical Machine Learning and XAI](/pmarupanthorn/research/ai-and-machine-learning-in-finance-and-insurance/)** — robust, interpretable predictive models for finance and insurance.
        - **[Stochastic Models in Financial and Insurance Technology](/pmarupanthorn/research/monte-carlo-simulation/)** — simulation, stochastic processes, computational finance, and InsurTech.
  - block: collection
    id: papers
    content:
      title: Featured Publications
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
        - **WorldQuant BRAIN Gold Level**, [Certificate of Accomplishment](/pmarupanthorn/uploads/worldquant-brain-gold-certificate.png)

        **Current site portfolio:** 15 publications and working papers · 44 talks and workshops · 10 courses · 9 research themes
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
