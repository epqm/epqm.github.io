---
layout: default
---
<div class="epqm-description">
## Emergent Phenomena in Quantum Matter
{{ site.description }}
</div>


<div class="home-header"><h1>Publication News</h1><a class="button notice" href="/posts#publication-news">See All News</a>
</div>
{% for post in site.categories["manuscript"] limit:4 %}
{% assign date = post.date | date: "%b %Y" | upcase %}
{% include update-item.html title=post.title date=date url=post.url excerpt=post.excerpt full=false %}
{% endfor %}


<div class="home-header"><h1>Updates</h1><a class="button notice" href="/posts#updates">See All Updates</a>
</div>

{% for post in site.categories["news"] limit:4 %}
{% assign date = post.date | date: "%b %Y" | upcase %}
{% include update-item.html title=post.title date=date url=post.url excerpt=post.excerpt full=false %}
{% endfor %}

# The Good Stuff

# Like What You see so far?
- Take a look at our [research interests](/research/) and [publications](/publications/) to get a better idea of what we do. 

- We have also uploaded some of our [seminars](/seminars/) on various topics in quantum condensed matter physics.

- If you want to get in touch with us, here are our [contact details](/about/#contact-details). If you are interested in joining us, please look at [openings](/about/#openings).
