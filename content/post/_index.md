---
title: Blogs
type: landing
cascade:
  - _target:
      kind: page
    params:
      show_breadcrumb: true
sections:
  - block: collection
    id: post
    content:
      title: Blogs
      count: 20
      filters:
        folders:
          - post
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
