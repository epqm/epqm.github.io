---
permalink: /publications/
layout: single
classes: wide
title: "EPQM's Publications & Preprints"

---

{% for work in site.data.publications %}
- {% include publication_info.html %}
{% endfor %}
