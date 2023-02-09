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
      url: /about/#openings

---

{% for post in site.posts %}
{% if post.pinned == true %}
### <i class="fas fa-thumbtack fontawesome__icon"></i> Pinned Post
<div class="feature__wrapper">
{% include feature_row_posts %}
</div>
{% break %}
{% endif %}
{% endfor %}

<div class="home__column" markdown=1>
## <i class="fas fa-bookmark"></i>&nbsp;&nbsp;[Recent Articles & Preprints](/posts/)

{% assign counter = 0 %}
{% for post in site.posts %}
{% if post.categories contains "publication" or post.categories contains "preprint" %}
{% include feature_row_posts type="center" %}
{% assign counter = counter | plus:1 %}
{% if counter == 3 %}
{% break %}
{% endif %}
{% endif %}
{% endfor %}

## <i class="fas fa-bolt"></i>&nbsp;&nbsp;[Recent Updates](/posts/)

{% assign counter = 0 %}
{% for post in site.posts %}
{% unless post.categories contains "publication" or post.categories contains "preprint" %}
{{ post.header }}
{% include feature_row_posts type="center" %}
{% assign counter = counter | plus:1 %}
{% if counter == 3 %}
{% break %}
{% endif %}
{% endunless %}
{% endfor %}

</div>

<div class="home__column" markdown=1>

<h2 markdown=1 id="highlights"><i class="fas fa-bullhorn"></i>&nbsp;&nbsp;Some Highlights</h2>

{% include highlights.html %}
</div>
