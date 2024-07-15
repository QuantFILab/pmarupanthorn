---
title: Teaching
summary: My courses
type: landing

cascade:
  - _target:
      kind: page
    params:
      show_breadcrumb: true
      paginate: -1  # Disable pagination by setting to -1
sections:
  - block: collection
    id: teaching
    content:
      title: Teaching
      filters:
        folders:
          - teaching
    design:
      view: article-grid
      columns: 4
      params:
        paginator: 0  # Show all items by setting paginator to 0
---
