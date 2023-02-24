---
permalink: /posts/
classes: wide
author_profile: false
title: "EPQM: All Updates and Notifications from the group"
excerpt: All news regarding publications, conferences and other activity in the group
header:
    overlay_image: /assets/images/updates/updates_header.svg

---

{% for post in site.posts %}
{% assign rem = forloop.index | modulo: 2 %}
{% if rem == 0 %}
{% include feature_row_posts type="left" %}
{% else %}
{% include feature_row_posts type="right" %}
{% endif %}
{% endfor %}
