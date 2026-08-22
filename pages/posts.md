---
permalink: /posts/
title: "EPQM: All Updates and Notifications from the group"
excerpt: All news regarding publications, conferences and other activity in the group
toc: true
---

## Research Updates
{% for post in site.categories["manuscript"] %}
### {{ post.title }}

<div class="seminar-details"><p><a href="{{ post.url }}" class="button">Learn More</a>{{ post.date | date: "%b %d, %Y" }}</p></div>
{% endfor %}

## Miscellaneous News
{% for post in site.categories["updates"] %}
### {{ post.title }}

<div class="seminar-details"><p><a href="{{ post.url }}" class="button">Learn More</a>{{ post.date | date: "%b %d, %Y" }}</p></div>
{% endfor %}
