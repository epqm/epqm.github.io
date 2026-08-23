---
permalink: /publications/
title: "EPQM: Publications and Preprints"
---

<a class="button" href="https://arxiv.org/search/?searchtype=author&query=Lal%2C+Siddhartha">Arxiv</a>
<a class="button" href="https://scholar.google.co.in/citations?user=QRSxh6kAAAAJ&hl=en">Google Scholar</a>

{% for item in site.data.publications %}
{% assign authors = item.authors | join: ", " %}
{% include update-item.html title=item.title date=item.reference url=item.url excerpt=authors %}
{% endfor %}
