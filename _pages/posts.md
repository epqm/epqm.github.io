---
permalink: /posts/
layout: splash
author_profile: false
title: "EPQM: All Updates and Notifications from the group"
excerpt: All news regarding publications, conferences and other activity in the group
header:
    overlay_image: /assets/images/updates/updates_header.svg
    actions:
        - label: Publication updates
          url: /posts/#publication-and-preprint-updates
        - label: Other news
          url: /posts/#miscellaneous-news

---

# Jump to

- [PUBLICATION/PREPRINT UPDATES](/posts/#publication-and-preprint-updates)

- [MISCELLANEOUS NEWS](/posts/#miscellaneous-news)

# Publication and preprint updates
{% for post in site.posts %}
{% if post.categories[0] == "publications-and-preprints" %}
{% include feature_row_posts.html type="left" show_tags="true" %}
{% endif %}
{% endfor %}

# Miscellaneous news
{% for post in site.posts %}
{% if post.categories[0] == "updates" %}
- **{{ post.title }}**&nbsp;&nbsp;<a href="{{ post.url | relative_url }}" class="btn btn--danger">{{ post.btn_label | default: site.data.ui-text[site.locale].more_label | default: "Learn More" }}</a><br>{{ post.date | date: "%b %d, %Y" | upcase }}

{% endif %}
{% endfor %}
