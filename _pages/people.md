---
permalink: /people/
layout: single
title: "EPQM Members: Present Team and Alumni"
classes: wide
header:
    overlay_image: /assets/images/people/people_header.jpg
    caption: "[Source](https://phdcomics.com/comics.php?f=1760)"

---

# Group members

{% for class in site.data.people %}

## {{ class[0] }}

{% include feature_row_people.html %}

{% endfor %}

{% include gallery %}

