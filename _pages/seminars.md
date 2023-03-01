---
permalink: /seminars/
layout: single
classes: wide
title: "EPQM: Seminars and Other Presentations"
excerpt: "Includes slides and video when available"
header:
    overlay_image: /assets/images/seminars/seminars_header.svg
    caption: "[Source](https://phdcomics.com/comics/archive.php/archive_print.php?comicid=1630)"

---

{% for seminar in site.data.seminars %}

{{ forloop.index }}.&nbsp;&nbsp;**{{ seminar.title }}**<br>
<i class="fas fa-paper-plane"></i>&nbsp;&nbsp;{{ seminar.location }}<br>
<i class="far fa-calendar-alt"></i>&nbsp;&nbsp;{{ seminar.date | date:"%b %d, %Y" }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
{%- if seminar.video_url -%}[Video]({{ seminar.video_url }}){:.btn .btn--primary}{% endif %}
{% if seminar.slides_url -%}
[Slides]({{ site.url }}{{ site.baseurl }}{{ seminar.slides_url }}){:.btn .btn--warning .tag__highlight}
<span class="pdf__preload"><img src="{{ site.url }}{{ site.baseurl }}{{ seminar.slides_url }}"></span>
{%- endif -%}

{%- if seminar.comments -%}<span class="seminar__comments" markdown=1>**Comments**: {{ seminar.comments }}</span>{%- endif -%}


{% endfor %}
