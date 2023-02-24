---
permalink: /posts/
layout: splash
classes: wide
author_profile: false
title: "EPQM: All Updates and Notifications from the group"
excerpt: All news regarding publications, conferences and other activity in the group
header:
    overlay_image: /assets/images/updates/updates_header.svg
    caption: "[Source](https://phdcomics.com/comics/archive.php/archive/archive_print.php?comicid=1366)"

---

{% for post in site.posts %}
{% include feature_row_posts type="left" %}
{% endfor %}
