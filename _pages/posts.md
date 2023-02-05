---
permalink: /posts/
layout: single
classes: wide
title: All Posts

---

{% for post in site.posts %}
- <a class="hover-underline-animation" style="text-decoration: none;" href="{{ post.url }}">{{ post.title }}</a><br>
<span class="pub__authors">{{ post.excerpt }}<br>
<i class="fa-solid fa-tags"></i> {%- for tag in post.tags -%} <span class="btn btn--inverse tag__highlight">{{ tag }}</span>{%- endfor -%}<br></span>
<i class="far fa-calendar-alt"></i> &nbsp;&nbsp;&nbsp;<span>{{ post.date | date:"%B %d, %Y"  }}</span>
<br>
{% endfor %}
