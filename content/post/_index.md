---
widget: portfolio
title: Blogs
type: landing
cascade:
  - _target:
      kind: page
    params:
      show_breadcrumb: true
sections:
  - block: tag_cloud
    content:
      title: My title
      subtitle: My subtitle
      text: Add any **markdown** formatted content here - text, images, videos, galleries - and even HTML code!
      # Choose a taxonomy from the `taxonomies` list in `config.yaml` to display (e.g. tags, categories, authors)
      taxonomy: tags
      # Choose how many tags you would like to display (0 = all tags)
      count: 20
    design:
      # Minimum and maximum font sizes (1.0 = 100%).
      font_size_min: 0.7
      font_size_max: 2.0
sections:
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
