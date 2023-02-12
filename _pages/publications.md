---
permalink: /publications/
layout: single
classes: wide
title: "EPQM: Publications and Preprints"
excerpt: "Click on the journal DOI or the arxiv link of the work to access the manuscript."
header:
    overlay_image: /assets/images/publications/publications.jpg
    overlay_filter: 0.3

---

<div class="slideshow-container" markdown=1>

<div class="dot__sliding" id="dot__sliding" markdown=1>
<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
{%- for i in (1..6) -%}
&nbsp;<a href="{{ page.permalink }}#highlights" class="dot" onclick="currentSlide({{ i }})"></a>&nbsp;
{%- endfor -%}
<a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>
{% assign pages = site.data.publications | size | divided_by: 6 %}
{% for page in (0..pages) %}
{% assign first = page | times: 6 %}
<div class="mySlides fade" markdown=1>
<span class="dot_caption"><b>{{ first | plus: 1 }} - {{ first | plus: 6 }}</b></span>
{% for work in site.data.publications offset: first limit: 6 %}
{% include publication_info.html %}
{% endfor %}
</div>
{% endfor %}

</div>

<div class="dot__sliding" markdown=1>
<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
{%- for i in (1..6) -%}
&nbsp;<a href="{{ page.permalink }}#highlights" class="dot" onclick="currentSlide({{ i }})"></a>&nbsp;
{%- endfor -%}
<a href="{{ page.permalink }}#highlights" class="next" onclick="plusSlides(1)">&#10095;</a>
</div>
