---
layout: splash
title: Emergent Phenomena in Quantum Matter
excerpt: You have reached the website of **EPQM**, a theoretical research group in the Department of Physics at IISER Kolkata, led by Siddhartha Lal. We focus on quantum condensed matter physics.
header:
    overlay_image: /assets/images/home2.svg
    actions:
    - label: "About"
      url: /about/
    - label: "Research"
      url: /research/
    - label: "People"
      url: /people/
---

{% for post in site.posts %}
{% if post.pinned == true %}
## <i class="fas fa-thumbtack fontawesome__icon"></i> Pinned Post
<div class="feature__wrapper">
{% include feature_row_posts %}
</div>
{% break %}
{% endif %}
{% endfor %}

## Recent Posts
{% include feature_row_posts type="left" %}

{% include selected_publications.html %}