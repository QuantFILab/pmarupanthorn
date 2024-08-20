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
        <a href="https://quantfilab.github.io/pmarupanthorn/tags/sustainable-finance/" style="background-color: #0b3d0b; color: #fff; padding: 2px 4px; border-radius: 3px; text-decoration: none;">#Investment</a>
        <a href="https://quantfilab.github.io/pmarupanthorn/tags/large-language-model/" style="background-color: #0b3d0b; color: #fff; padding: 2px 4px; border-radius: 3px; text-decoration: none;">#Financial Product</a>
      count: 20
      filters:
        folders:
          - post
      buttons:
        - name: All
          tag: '*'
        - name: Deep Learning
          tag: Deep Learning
        - name: Other
          tag: Demo
    design:
      view: masonry
---
