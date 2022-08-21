---
permalink: /publications/
layout: single
title: Research Publications
---

{% for work in site.data.publications %}
{% include publication_info.html %}
<div style="display:block;height:2em;"></div>
{% endfor %}
