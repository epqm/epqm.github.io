---
layout: splash
title: "Emergent Phenomena in Quantum Matter (EPQM)"
excerpt: "EPQM is a condensed matter group at IISER Kolkata, led by Siddhartha Lal. We explore ideas related to quantum matter in the fields of strongly correlated electrons, quantum magnetism, topological states of matter and low-dimensional systems."
header:
    overlay_image: /assets/images/home/layered-waves-haikei.svg

---

# <i class="fas fa-bookmark"></i>&nbsp;&nbsp;[Recent Articles & Preprints](/posts/)
<div style="display: block; overflow:hidden;">
<div class="home__column" markdown=1>
{% assign post = site.categories["publications and preprints"][0] %}
{% include feature_row_posts type="center" %}
</div>
<div class="home__column" markdown=1>
{% assign post = site.categories["publications and preprints"][2] %}
{% include feature_row_posts type="center" %}
</div>
</div>
<div style="display: block; overflow:hidden;">
<div class="home__column" markdown=1>
{% assign post = site.categories["publications and preprints"][1] %}
{% include feature_row_posts type="center" %}
</div>
<div class="home__column" markdown=1>
{% assign post = site.categories["publications and preprints"][3] %}
{% include feature_row_posts type="center" %}
</div>
</div>

# <i class="fas fa-bolt"></i>&nbsp;&nbsp;[Recent Updates](/posts/)

<div style="display: block; overflow:hidden;">
<div class="home__column" markdown=1>
{% assign post = site.categories["updates"][0] %}
{% include feature_row_posts type="center" %}
</div>
<div class="home__column" markdown=1>
{% if site.categories["updates"].size > 1 %}
{% assign post = site.categories["updates"][1] %}
{% include feature_row_posts type="center" %}
{% endif %}
</div>
</div>

<h1 markdown=1 id="highlights"><i class="fas fa-bullhorn"></i>&nbsp;&nbsp;Some Highlights</h1>

{% include highlights.html %}
