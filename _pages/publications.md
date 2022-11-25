---
permalink: /publications/
layout: single
title: Research Publications
---

<div style="width: 48%;float:left;margin:auto;">
{% for work in site.data.publications %}
{% assign mod = forloop.index | modulo: 2 %}
{% if mod == 0 %}
{% continue %}
{% endif %}
{% include publication_info.html pre_text=forloop.index %}
{% endfor %}
</div>
<div style="width: 48%;float:right;margin:auto;">
{% for work in site.data.publications %}
{% assign mod = forloop.index | modulo: 2 %}
{% if mod == 1 %}
{% continue %}
{% endif %}
{% include publication_info.html pre_text=forloop.index %}
{% endfor %}
</div>
