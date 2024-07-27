---
title: Blogs
type: landing
cascade:
  - _target:
      kind: page
    params:
      show_breadcrumb: true
sections:
  - block: markdown
    content:
      title: Tags 
      text: |
        - [Hugo Documentation](https://gohugo.io/documentation/)
        - [Hugo Themes](https://themes.gohugo.io/)
  - block: collection
    id: post
    content:
      title: Blogs
      count: 20
      filters:
        folders:
          - post
    design:
      view: article-grid
      columns: 3
      fill_image: false
---
