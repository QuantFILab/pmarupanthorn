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
