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
      text: |
        The default blogs are written in English. If you are looking for content in Thai, please follow the link provided within the blogs.
      count: 100
      filters:
        folders:
          - post
    design:
      view: article-grid
      columns: 3
      fill_image: false
---
