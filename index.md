---
layout: default
---
<div class="epqm-description">
## Emergent Phenomena in Quantum Matter
{{ site.description }}
</div>


<div class="home-header"><h1>Publication News</h1><a class="button notice" href="/posts#research-updates">See All News</a>
</div>
{% for post in site.categories["manuscript"] limit:4 %}
{% include update-item.html post=post full=false %}
{% endfor %}


<div class="home-header"><h1> Miscellaneous News</h1><a class="button notice" href="/posts#miscellaneous-news">See All Updates</a>
</div>

{% for post in site.categories["news"] limit:4 %}
{% include update-item.html post=post %}
{% endfor %}

# The Good Stuff

# Like What You see so far?
- Take a look at our [research interests](/research/) and [publications](/publications/) to get a better idea of what we do. 

- We have also uploaded some of our [seminars](/seminars/) on various topics in quantum condensed matter physics.

- If you want to get in touch with us, here are our [contact details](/about/#contact-details). If you are interested in joining us, please look at [openings](/about/#openings).
