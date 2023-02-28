---
permalink: /posts/
layout: splash
author_profile: false
title: "EPQM: All Updates and Notifications from the group"
excerpt: All news regarding publications, conferences and other activity in the group
header:
    overlay_image: /assets/images/updates/updates_header.svg

---

{% for post in site.posts %}
{% include feature_row_posts type="left" show_tags="true" %}
{% endfor %}
