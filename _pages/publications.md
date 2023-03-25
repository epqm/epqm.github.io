---
permalink: /publications/
layout: single
classes: wide
title: "EPQM: Publications and Preprints"
excerpt: "Click on the journal DOI or the arxiv link of the work to access the manuscript."
header:
    overlay_image: /assets/images/seminars/seminars_header.svg

---

<span class="pub__external__links">[ARXIV LINK](https://arxiv.org/search/?searchtype=author&query=Lal%2C+Siddhartha){: .btn .btn--info } [G. SCHOLAR](https://scholar.google.co.in/citations?user=QRSxh6kAAAAJ&hl=en){: .btn .btn--info }</span>

{% assign slides_per_page = 6 %}
{% assign pub_data = site.data.publications %}
{% assign rem = pub_data.size | modulo:slides_per_page %}
{% if rem == 0 %}
{% assign num_slides = pub_data.size | divided_by:slides_per_page %}
{% else %}
{% assign num_slides = pub_data.size | divided_by:slides_per_page | plus: 1 %}
{% endif %}

<div class="slider__dots">
<a class="slide__arrow" id="slide__prev__1"><i class="fas fa-chevron-left" onclick="switch_slide(-1)"></i></a>&nbsp;
{% for i in (1..num_slides) %}
<a class="slider__dot" id="slider__dot__{{ forloop.index }}" onclick="show_slide()"></a>
{% endfor %}
&nbsp;<a class="slide__arrow" id="slide__next__1"><i class="fas fa-chevron-right" onclick="switch_slide(1)"></i></a>
</div>
{% for i in (1..num_slides) %}
{% assign off_set = forloop.index | minus:1 | times: slides_per_page %}
<div class="pub_slide" id="pub_slide_{{ forloop.index }}" markdown=1>
[ **{{ off_set | plus:1 }} - {{ off_set | plus:slides_per_page }}** ]
{: .text-center }
{% for work in pub_data offset:off_set limit:slides_per_page %}<hr>{% include publication_info.html readmore="True" %}{% endfor %}
</div>
{% endfor %}
