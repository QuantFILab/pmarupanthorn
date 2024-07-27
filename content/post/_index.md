---
title: Blogs
type: landing
cascade:
  - _target:
      kind: page
    params:
      show_breadcrumb: true
sections:
  - block: tags
    content:
      title: Tags
    
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
