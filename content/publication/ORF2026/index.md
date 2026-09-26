---
title: "State Conditional Boosting for Prospective Early Warning of CFPB Reported Relief Workload"
authors:
- Nassamon Bootwisas
- admin
date: "2026-09-12T00:00:00Z"
doi: "https://doi.org/10.1007/s43069-026-00695-2"

# Schedule page publish date (NOT publication's date).
publishDate: "2026-09-12T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Operations Research Forum, 7, 106, 2026*"
publication_short: "*Oper. Res. Forum*"

abstract: Consumer complaint records can help prioritize supervisory review, but they do not directly identify verified consumer harm. This study formulates a prospective company product review problem using a calendar-complete design and defines company-reported relief as the primary observable workload marker. The state conditional representation distinguishes ordinary activity, relief count escalation, overlapping count and composition escalation, and excess relief composition. The evaluation includes explicit persistence rules, a global recurrent negative binomial forecaster, alternative boosted tree learners, probability calibration, model confidence sets, rolling target boundaries, drift diagnostics, periodic refitting, and global and local Shapley contributions. Delayed relief persistence recovers much of the event ranking signal, although matched boosting retains incremental value. The state representation improves pooled excess relief discrimination under LightGBM and XGBoost but not CatBoost, and weekly capacity comparisons do not identify a unique winner. The evidence supports administrative review prioritization among established high activity cells rather than verified harm detection or universal model superiority.

# Summary. An optional shortened abstract.
summary: ""

tags:
- Statistical Machine Learning
- Explainable AI
- Early Warning Systems
- Consumer Finance
featured: true

url_pdf: https://link.springer.com/article/10.1007/s43069-026-00695-2
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

image:
  caption: "Model ranking, calibration, and XGBoost state contributions."
  focal_point: Center
  preview_only: false

projects: []
slides: ""
---
