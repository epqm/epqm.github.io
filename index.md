---
layout: default
---
<div class="epqm-description">
## Emergent Phenomena in Quantum Matter
{{ site.description }}
</div>


# Publication News

<a class="button notice" href="/updates/">See All News</a>

{% for post in site.categories["manuscript"] limit:4 %}
### {{ post.title }}
**{{ post.date | date: "%b %d, %Y" }}.**
{{ post.excerpt }} <a class="button" href="{{ post.url }}">Read More</a>
{% endfor %}

# Miscellaneous News


<a class="button notice" href="/updates/">See All News</a>

{% for post in site.categories["news"] limit:4 %}
### {{ post.title }}
**{{ post.date | date: "%b %d, %Y" }}.**
{{ post.excerpt }} <a class="button" href="{{ post.url }}">Read More</a>
{% endfor %}

# The good stuff

# Like what you see so far?
- Take a look at our [research interests](/research/) and [publications](/publications/) to get a better idea of what we do. 

- We have also uploaded some of our [seminars](/seminars/) on various topics in quantum condensed matter physics.

- If you want to get in touch with us, here are our [contact details](/about/#contact-details). If you are interested in joining us, please look at [openings](/about/#openings).
