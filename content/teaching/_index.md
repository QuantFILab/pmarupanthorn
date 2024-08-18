---
title: Teaching
type: landing
cascade:
  - _target:
      kind: page
    params:
      show_breadcrumb: true
sections:
  - block: collection
    id: teaching
    content:
      title: Teaching
      count: 0
      filters:
        folders:
          - teaching
        filter_button:
          - name: All
            tag: '*'
          - name: Deep Learning
            tag: Deep Learning
          - name: Other
            tag: Demo

  # Default filter toolbar button (e.g. 0 corresponds to the first `filter_button` instance above)
  filter_default: 0
    design:
      view: article-grid
      columns: 3
      fill_image: false
  
---
