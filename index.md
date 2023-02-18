---
layout: splash
title: "Emergent Phenomena in Quantum Matter (EPQM)"
excerpt: "EPQM is a condensed matter group at IISER Kolkata, led by Siddhartha Lal. We explore ideas related to quantum matter in the fields of strongly correlated electrons, quantum magnetism, topological states of matter and low-dimensional systems."
header:
    overlay_image: /assets/images/home/layered-waves-haikei.svg
    actions:
    - label: Openings
      url: /about/#openings
    - label: Contacts
      url: /about/#contact-details
    - label: EPQM in a Nutshell
      url: /about/#what-is-epqm

---

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
