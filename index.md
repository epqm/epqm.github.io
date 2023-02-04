---
layout: splash
title: Emergent Phenomena in Quantum Matter
excerpt: You have reached the website of *EPQM*, a theoretical condensed matter research group at IISER Kolkata, led by *Siddhartha Lal*.
header:
    overlay_image: /assets/images/stacked-steps-haikei.svg
    actions:
    - label: "About"
      url: /about/
    - label: "Research"
      url: /research/
    - label: "People"
      url: /about/#group-members
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
