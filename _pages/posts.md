---
permalink: /posts/
layout: single
classes: wide
author_profile: false
title: "EPQM: All Updates and Notifications from the group"
excerpt: All news regarding publications, conferences and other activity in the group
header:
    overlay_image: /assets/images/updates/updates_header.svg
    caption: "[Source](https://phdcomics.com/comics/archive.php/archive/archive_print.php?comicid=1366)"

---

{% for post in site.posts %}
- <a class="hover-underline-animation" style="text-decoration: none;" href="{{ post.url }}">{{ post.title }}</a><br>
<span class="pub__authors">
{%- unless post.excerpt == "" -%}
{{ post.excerpt }}<br>
{%- endunless -%}
<i class="fas fa-tags"></i>&nbsp;&nbsp;{%- for tag in post.tags -%}<span class="btn btn--primary tag__highlight">{{ tag }}</span>{%- endfor -%}<br></span>
<i class="far fa-calendar-alt"></i> &nbsp;&nbsp;<span>{{ post.date | date:"%B %d, %Y"  }}</span>
<br>
{% endfor %}
