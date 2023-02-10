---
permalink: /publications/
layout: single
classes: wide
title: "EPQM: Publications and Preprints"
excerpt: "Click on the journal DOI or the arxiv link of the work to access the manuscript."
header:
    overlay_image: /assets/images/publications/publications.jpg
    overlay_filter: 0.3
    actions:
    - label: "Research"
      url: /research/
    - label: "RGate"
      url: "https://www.researchgate.net/profile/Siddhartha-Lal-2"

---

A description of our research interests can be found [here](/research/).

{% for work in site.data.publications %}

{% include publication_info.html %}

{% endfor %}
