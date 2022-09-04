---
permalink: /posts/
layout: single
classes: wide
title: All Posts

---

{% for post in site.posts %}
{{ forloop.index }}. <a class="hover-underline-animation" style="text-decoration: none;" href="{{ post.url }}">{{ post.title }}</a><br>
{{ post.excerpt }}<br>
<i class="far fa-calendar-alt"></i> <span>{{ post.date | date:"%B %d, %Y"  }} </span>
{% endfor %}
