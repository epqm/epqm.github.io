---
layout: splash
title: Emergent Phenomena in Quantum Matter
excerpt: You have reached the website of *EPQM*, a theoretical condensed matter research group at IISER Kolkata, led by *Siddhartha Lal*.
header:
    overlay_image: /assets/images/layered-waves-haikei.svg
    actions:
    - label: About
      url: /about/
    - label: Publications
      url: /publications/
    - label: Openings
      url: /openings/

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

## Recent Updates [[see all]](/posts/){:.btn}

{% include feature_row_posts type="left" %}

{% assign post = site.posts[0] %} 
{% assign work = site.data.publications[0] %}

<div class="home__column" markdown=1>
## Highlight: [{{ work["title"] }}]({{ post.url }})

{% assign show_publication_title = 'False' %}
{% include publication_info.html show_tags=1 %}
{% assign show_publication_title = nil %}

{{ post.content }}
</div>
<div class="home__column" markdown=1>
{% include selected_publications.html %}
</div>
