---
layout: splash
feature_row:
feature_row:
  - image_path: /assets/images/thumb1.jpeg
    title: Gallery
    excerpt: "Check out the gallery for some photographs of our group as well as the IISER Kolkata campus."
    url: /gallery/
    btn_label: "Read More"
    btn_class: "btn btn--danger"
  - image_path: /assets/images/thumb2.jpeg
    title: External resources
    excerpt: "Take a look at our suggested external resources for interesting content pertaining to physics or academia in general."
    url: /external-resources/
    btn_label: "Read More"
    btn_class: "btn btn--danger"
  - image_path: /assets/images/thumb3.jpg
    title: Fiction suggestions
    excerpt: "Check out our recommendations for a single work of fiction that should be experienced by everyone at least once."
    url: /fiction-recommendations/
    btn_label: "Read More"
    btn_class: "btn btn--danger"

---

{% assign num_slides = 6 %}
{% for post in site.categories["publications-and-preprints"] limit:num_slides %}

{% for work in site.data.publications %}
{% if work.last["permalink"] == post.permalink %}{% assign abstract = work.last["abstract"] %}{% endif %}
{% endfor %}

{% assign next_slide_num = forloop.index | plus:1 %}
{% assign prev_slide_num = forloop.index | minus:1 %}
{% if forloop.index == num_slides %}{% assign next_slide_num = 1 %}{% endif %}
{% if forloop.index == 1 %}{% assign prev_slide_num = num_slides %}{% endif %}

<div class="pub_slide fade" id="pub_slide_{{ forloop.index }}" markdown=1>
[![]({% if post.header["overlay_image"] %}{{ post.header["overlay_image"] }}{% else %}{{ post.header["image"] }}{% endif %})]({{ post.url }}){: .home_banner_image }

<div class="home__column__main" markdown=1>
<div class="home__column_skewed" markdown=1>
<span class="btn btn--success" onclick="show_highlight({{ prev_slide_num }})"><span class="fas fa-chevron-left"></span>&nbsp;&nbsp;Prev</span>&nbsp;&nbsp;<span class="btn btn--success" onclick="show_highlight({{ next_slide_num }})">Next&nbsp;&nbsp;<span class="fas fa-chevron-right"></span></span>

{{ post.title }}
{: .home__banner__title}

{{ abstract | split:". " | slice: 0,2 | join: ". " | append: "." }}
{: .archive__item-excerpt }

[Learn More]({{ post.url }}){: .btn .btn--danger }
</div>

<div class="home__column_skewed" markdown=1>

<div class="notice--info " markdown=1>
# Emergent Phenomena in Quantum Matter

<span class="epqm__description">{{ site.description }}</span>

</div>

[EPQM in a nutshell](/about/#what-is-epqm){: .btn .btn--primary }
[Research](/research/#overview-of-our-research){: .btn .btn--primary }
[Members](/people){: .btn .btn--primary }

![](./assets/images/about/epqm_logo_combined.svg){: .align-center}

</div></div></div>
{% endfor %}

## <i class="fas fa-bookmark"></i>&nbsp;&nbsp;Publication News

[See all news](/posts/#publication-and-preprint-updates){: .btn .btn--info }

<div class="home__column__main" markdown=1>
{% for post in site.categories["publications-and-preprints"] limit:2 %}
  <div class="home__column" markdown=1>
  {% include feature_row_posts.html type="center" %}
  </div>
  {% endfor %}
</div>
<div class="home__column__main" markdown=1>
  {% for post in site.categories["publications-and-preprints"] offset:2 limit:2 %}
  <div class="home__column" markdown=1>
  {% include feature_row_posts.html type="center" %}
  </div>
  {% endfor %}
</div>

## <i class="fas fa-bolt"></i>&nbsp;&nbsp;Miscellaneous News

[See all news](/posts/#miscellaneous-news){: .btn .btn--info }

{% for post in site.categories["updates"] limit:3 %}
- **{{ post.title }}**&nbsp;&nbsp;<a href="{{ post.url | relative_url }}" class="btn btn--danger">Learn More</a>&nbsp;&nbsp;{{ post.date | date: "%b %d, %Y" | upcase }}
{% endfor %}

## <i class="fas fa-heart"></i>&nbsp;&nbsp;The good stuff
{% include feature_row %}

## <i class="fas fa-mug-hot"></i>&nbsp;&nbsp;Like what you see so far?
- Take a look at our [research interests](/research/) and [publications](/publications/) to get a better idea of what we do. 

- We have also uploaded some of our [seminars](/seminars/) on various topics in quantum condensed matter physics.

- If you want to get in touch with us, here are our [contact details](/about/#contact-details). If you are interested in joining us, please look at [openings](/about/#openings).

[Research](/research/){: .btn .btn--info }
[Seminars](/seminars/){: .btn .btn--info }
[Contact](/about/#contact-details){: .btn .btn--info }

{% include footer/home_slides.html %}
