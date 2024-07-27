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
      title: Tags and Categories
      text: |
        ## Tags
        {{< list_tags >}}
        
        ## Categories
        {{< list_categories >}}
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
