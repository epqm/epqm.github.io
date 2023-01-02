---
permalink: /people/
layout: splash
author_profile: false
title: Team members of EPQM
excerpt: Research scholars, masters students and alumni of the group

---

{% for class in site.data.people %}

## {{ class[0] }}

{% include feature_row_people.html %}

{% endfor %}
