---
layout: splash

---

[![]({{ site.categories["publications and preprints"][0].header["overlay_image"] }})]({{ site.categories["publications and preprints"][0].url }})
<div class="home__column__main" markdown=1>
 <div class="home__column_skewed" markdown=1>
  <div class="home__banner__title" markdown=1>
  {% assign letters = site.categories["publications and preprints"][0].title | split:"" %}
  <span class="first-letter">{{ letters[0] }}</span>{{ letters | shift}}
  </div> 
  <span class="home__banner__abstract" markdown=1> 
  {{ site.data.publications[0]["abstract"] | truncate:300 }}
  </span> &nbsp;&nbsp;[Learn More]({{ site.categories["publications and preprints"][0].url }}){: .btn .btn--danger }
 </div>
 <div class="home__column_skewed" markdown=1>
  <h2>Who are we?</h2>
  <span class="epqm_description">{{ site.description }}</span>

  [EPQM in a nutshell](/about/#what-is-epqm){: .btn .btn--primary }
  [Research](/research/#overview-of-our-research){: .btn .btn--primary }

  [Openings](/about/#openings){: .btn .btn--primary }
 </div>
</div>


## <i class="fas fa-bookmark"></i>&nbsp;&nbsp;[Recent Articles/Preprints](/posts/)
<div class="home__column__main" markdown=1>
 <div class="home__column" markdown=1>
 {% assign post = site.categories["publications and preprints"][0] %}
 {% include feature_row_posts type="center" %}
 </div>
 <div class="home__column" markdown=1>
 {% assign post = site.categories["publications and preprints"][2] %}
 {% include feature_row_posts type="center" %}
 </div>
</div>
<div class="home__column__main" markdown=1>
 <div class="home__column" markdown=1>
 {% assign post = site.categories["publications and preprints"][1] %}
 {% include feature_row_posts type="center" %}
 </div>
 <div class="home__column" markdown=1>
 {% assign post = site.categories["publications and preprints"][3] %}
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
