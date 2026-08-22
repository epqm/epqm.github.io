---
permalink: /posts/
---

# Research Updates
{% for post in site.categories["manuscript"] %}
{% include update-item.html post=post %}
{% endfor %}

# Miscellaneous News
{% for post in site.categories["news"] %}
{% include update-item.html post=post %}
{% endfor %}
