---
layout: splash

---

<div class="home_banner_image">
<a href="{{ site.categories["publications-and-preprints"][0].url }}">
{% assign post = site.categories["publications-and-preprints"][0] %}
{% if post.header["overlay_image"] %}<img src="{{ post.header["overlay_image"] }}">{% else %}<img src="{{ post.header["image"] }}">{% endif %}
</a>
</div>

<div class="home__column__main" markdown=1>
<div class="home__column_skewed" markdown=1>
<div class="home__banner__title" markdown=1>
{{ site.categories["publications-and-preprints"][0].title }}
</div> 
{% for pub in site.data.publications %}
{% if pub["permalink"] == site.categories["publications-and-preprints"][0].permalink %}
**{{ site.categories["publications-and-preprints"][0].date | date: "%b %d, %Y" | upcase }}**. <span class="home__banner__abstract">{{ pub["abstract"] | split:". " | slice: 0,2 | join: ". " | append: "." }}</span>
[Learn More]({{ site.categories["publications-and-preprints"][0].url }}){: .btn .btn--danger }
{% endif %}
{% endfor %}
</div>
<div class="home__column_skewed" markdown=1>

---
# Emergent Phenomena in Quantum Matter
<span class="home__banner__abstract">{{ site.description }}</span>

[EPQM in a nutshell](/about/#what-is-epqm){: .btn .btn--info }
[Research](/research/#overview-of-our-research){: .btn .btn--info }
[Members](/people){: .btn .btn--info }

---
</div>
</div>


## <i class="fas fa-bookmark"></i>&nbsp;&nbsp;Recent Articles/Preprints[[see all]](/posts/#publication-and-preprint-updates){: .btn }
<div class="home__column__main" markdown=1>
{% for post in site.categories["publications-and-preprints"] limit:2 %}
  <div class="home__column" markdown=1>
  {% include feature_row_posts type="center" %}
  </div>
  {% endfor %}
</div>
<div class="home__column__main" markdown=1>
  {% for post in site.categories["publications-and-preprints"] offset:2 limit:2 %}
  <div class="home__column" markdown=1>
  {% include feature_row_posts type="center" %}
  </div>
  {% endfor %}
</div>


## <i class="fas fa-bolt"></i>&nbsp;&nbsp;Miscellaneous News[[see all]](/posts/#miscellaneous-news){: .btn .btn--small }

{% for post in site.categories["updates"] limit:2 %}
- {{ post.date | date: "%b %d, %Y" | upcase }}. **{{ post.title }}**&nbsp;&nbsp;<a href="{{ post.url | relative_url }}" class="btn btn--danger">{{ post.btn_label | default: site.data.ui-text[site.locale].more_label | default: "Learn More" }}</a>
{% endfor %}
<br>

<div class="home__column__main" markdown=1>
<div class="home__column" markdown=1>
## <i class="fas fa-heart"></i>&nbsp;&nbsp;The good stuff

- Check out the [gallery](/gallery/) for some photographs of our group as well as the IISER Kolkata campus.

- Take a look at our recommended [external resources](/external-resources/) for funny/interesting/useful links pertaining to academia in general or (condensed matter) physics in particular.

- To pique your artistic side, each EPQM member has provided their recommendation for a single work of fiction which they believe should be experienced by everyone at least once. [Check them out!](/fiction-recommendations/)
</div>
<div class="home__column" markdown=1>
## <i class="fas fa-mug-hot"></i>&nbsp;&nbsp;Like what you see so far?
- Take a look at our [research interests](/research/) and [publications](/publications/) to get a better idea of what we do. 

- We have also put up a number of our [seminars](/seminars/) (slides/videos) on various topics in quantum condensed matter physics.

- If you want to get in touch with us for any reason, here are out [contact details](/about/#contact-details).

- Students who are interested in joining us can take a look at our [openings](/about/#openings).
</div>
