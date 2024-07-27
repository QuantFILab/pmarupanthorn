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
        <a href="https://gohugo.io/documentation/" style="background-color: #32CD32; color: #fff; padding: 2px 4px; border-radius: 3px; text-decoration: none;">#FinancialProduct</a>
      count: 20
      filters:
        folders:
          - post
    design:
      view: article-grid
      columns: 3
      fill_image: false
---
