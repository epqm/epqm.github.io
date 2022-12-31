---
permalink: /publications/
layout: single
title: Research Publications
header:
    image: /assets/images/pubs.svg
---

{% for work in site.data.publications %}
- {% include publication_info.html %}
{% endfor %}
