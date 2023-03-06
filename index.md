---
layout: splash

---

{% assign num_slides = 6 %}
{% for post in site.categories["publications-and-preprints"] limit:num_slides %}

{% for work in site.data.publications %}
{% if work["permalink"] == post.permalink %}{% assign abstract = work["abstract"] %}{% endif %}
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
{: .home__banner__title }

{{ abstract | split:". " | slice: 0,2 | join: ". " | append: "." }}
{: .home__banner__abstract }
[Learn More]({{ post.url }}){: .btn .btn--danger }
</div>

<div class="home__column_skewed" markdown=1>

<div class="notice--info" markdown=1>
# Emergent Phenomena in Quantum Matter

{{ site.description }}

[EPQM in a nutshell](/about/#what-is-epqm){: .btn .btn--info }
[Research](/research/#overview-of-our-research){: .btn .btn--info }
[Members](/people){: .btn .btn--info }

</div></div></div></div>
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
- {{ post.date | date: "%b %d, %Y" | upcase }}. **{{ post.title }}**&nbsp;&nbsp;<a href="{{ post.url | relative_url }}" class="btn btn--danger">{{ post.btn_label | default: site.data.ui-text[site.locale].more_label | default: "Learn More" }}</a>
{% endfor %}

<div class="home__column__main" markdown=1>
<div class="home__column" markdown=1>
## <i class="fas fa-heart"></i>&nbsp;&nbsp;The good stuff

- Check out the [gallery](/gallery/) for some photographs of our group as well as the IISER Kolkata campus.

- Take a look at our suggested [external resources](/external-resources/) for funny/interesting/useful links pertaining to academia in general or (condensed matter) physics in particular.

- Check out our [recommendations](/fiction-recommendations/) for "a single work of fiction that should be experienced by everyone at least once".

[Gallery](/gallery/){: .btn .btn--info }
[External Links](/external-resources/){: .btn .btn--info }
[Fiction Suggestions](/fiction-recommendations/){: .btn .btn--info }

</div>
<div class="home__column" markdown=1>
## <i class="fas fa-mug-hot"></i>&nbsp;&nbsp;Like what you see so far?
- Take a look at our [research interests](/research/) and [publications](/publications/) to get a better idea of what we do. 

- We have also uploaded some of our [seminars](/seminars/) on various topics in quantum condensed matter physics.

- If you want to get in touch with us, here are our [contact details](/about/#contact-details). If you are interested in joining us, please look at [openings](/about/#openings).

[Research](/research/){: .btn .btn--info }
[Seminars](/seminars/){: .btn .btn--info }
[Contact](/about/#contact-details){: .btn .btn--info }
</div>
