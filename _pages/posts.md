---
permalink: /posts/
layout: single
classes: wide
title: All Posts

---

{% for post in site.posts %}
{{ forloop.index }}. [**{{ post.title }}**]({{ post.url }})<br>
{{ post.excerpt }}<br>
<i class="far fa-calendar-alt"></i> <span>{{ post.date | date:"%B %d, %Y"  }} </span>
{% endfor %}
