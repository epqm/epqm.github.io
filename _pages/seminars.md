---
permalink: /seminars/
layout: single
classes: wide
title: "Siddhartha Lal: Seminars"
excerpt: "Includes slides and video when available"
header:
    overlay_image: /assets/images/seminars/seminars_header.jpg
    caption: "[Source](https://phdcomics.com/comics/archive.php/archive/archive_print.php?comicid=942)"
    actions:
    - label: Publications
      url: /publications/
    - label: About
      url: /about/

---

{% for seminar in site.data.seminars %}

{{ forloop.index }}.&nbsp;&nbsp;**{{ seminar.title }}**<br>
<i class="fas fa-paper-plane"></i>&nbsp;&nbsp;{{ seminar.location }}<br>
<i class="far fa-calendar-alt"></i>&nbsp;&nbsp;{{ seminar.date | date:"%b %d, %Y" }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
{%- if seminar.yt_id -%}[Video](https://www.youtube.com/watch?v={{ seminar.yt_id }}){:.btn .btn--primary .tag__highlight}&nbsp;&nbsp;{%- endif -%}
{%- if seminar.slides_url -%}[Slides]({{ site.url }}{{ site.baseurl }}{{ seminar.slides_url }}){:.btn .btn--warning .tag__highlight}{%- endif -%}
<span class="seminar__comments" markdown=1>**Comments**: {{ seminar.comments }}</span>

<div class="pdf__preload"><img src="{{ site.url }}{{ site.baseurl }}{{ seminar.slides_url }}"></div>

{% endfor %}
