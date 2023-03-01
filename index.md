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
<span class="home__banner__abstract" markdown=1> 
{{ site.categories["publications-and-preprints"][0].excerpt | truncate:300 }}
</span> &nbsp;&nbsp;[Learn More]({{ site.categories["publications-and-preprints"][0].url }}){: .btn .btn--danger }
</div>
<div class="home__column_skewed" markdown=1>
# *E*mergent *P*henomena in *Q*uantum *M*atter
<span class="epqm_description">{{ site.description }}</span>

[EPQM in a nutshell](/about/#what-is-epqm){: .btn .btn--info }
[Research](/research/#overview-of-our-research){: .btn .btn--info }
[Openings](/about/#openings){: .btn .btn--info }
</div>
</div>


## <i class="fas fa-bookmark"></i>&nbsp;&nbsp;[Recent Articles/Preprints](/posts/)
<div class="home__column__main" markdown=1>
 <div class="home__column" markdown=1>
 {% assign post = site.categories["publications-and-preprints"][1] %}
 {% include feature_row_posts type="center" %}
 </div>
 <div class="home__column" markdown=1>
 {% assign post = site.categories["publications-and-preprints"][2] %}
 {% include feature_row_posts type="center" %}
 </div>
</div>

## <i class="fas fa-bolt"></i>&nbsp;&nbsp;[Recent Updates](/posts/)
<div class="home__column__main" markdown=1>
{% for post in site.categories["updates"] limit:2 %}
<div class="home__column" markdown=1>
{% include feature_row_posts type="center" %}
</div>
{% endfor %}
</div>

## <i class="fas fa-heart"></i>&nbsp;&nbsp;The good stuff

- Check out the [gallery](/gallery/) for some photographs of our group as well as the IISER Kolkata campus.

- Take a look at our recommended [external resources](/external-resources/) for funny/interesting/useful links pertaining to academia in general or (condensed matter) physics in particular.

- To pique your artistic side, each EPQM member has provided their recommendation for a single work of fiction which they believe should be experienced by everyone at least once. [Check them out!](/fiction-recommendations/)
