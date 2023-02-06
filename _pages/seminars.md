---
permalink: /seminars/
layout: single
classes: wide
title: "Siddhartha Lal: Seminars"

---

{% for seminar in site.data.seminars %}

- **{{ seminar.title }}**<br>
<i class="fas fa-globe"></i>&nbsp;&nbsp;{{ seminar.location }}<br>
<i class="far fa-calendar-alt"></i>&nbsp;&nbsp;{{ seminar.date | date:"%b %d, %Y" }}&nbsp;&nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-link"></i>&nbsp;&nbsp;
{%- if seminar.yt_id -%}[Video link](https://www.youtube.com/watch?v={{ seminar.yt_id }}),&nbsp;&nbsp;{%- endif -%}
{% if seminar.slides_url %}[Slides]({{ seminar.slides_url }}) (example slides){% endif %}
{% if seminar.yt_id %}<div class="yt__embed">{% include video id=seminar.yt_id provider="youtube" %}</div>{% endif %}
{% if seminar.slides_url %}<div class="yt__embed"><object data="{{ site.url }}{{ site.baseurl }}{{ seminar.slides_url }}#view=FitH" width="1200" height="800" type="application/pdf"></object></div>{% endif %}

{% endfor %}

