---
permalink: /publications/
layout: single
classes: wide
title: "EPQM's Publications & Preprints"

---

A description of our research interests can be found [here](/research/).

{% for work in site.data.publications %}
- {% include publication_info.html %}
{% endfor %}
