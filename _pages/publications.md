---
permalink: /publications/
layout: single
classes: wide
title: Research Publications
header:
    image: /assets/images/pubs.svg
---

{% for work in site.data.publications %}
- {% include publication_info.html %}
{% endfor %}
