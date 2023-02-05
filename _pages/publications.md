---
permalink: /publications/
layout: single
classes: wide
title: "Our Publications and Preprints: Complete List"
excerpt: "Click on the journal DOI or the arxiv link of the work to learn more about it."
header:
    overlay_image: /assets/images/posts/mott_MERG.svg
    overlay_filter: 0.5
    actions:
    - label: "research interests"
      url: /research/
    - label: "ResearchGate"
      url: "https://www.researchgate.net/profile/Siddhartha-Lal-2"

---

A description of our research interests can be found [here](/research/).

{% for work in site.data.publications %}

{% include publication_info.html %}

{% endfor %}
