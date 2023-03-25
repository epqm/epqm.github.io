---
permalink: /fiction-recommendations/
classes: wide
title: "EPQM recommendations: Remarkable works of fiction"
excerpt: "Works of fiction that we feel everyone should experience at least once"
header:
    overlay_image: /assets/images/seminars/seminars_header.svg

---

We asked EPQM members to contribute a single work of fiction that they feel is remarkable and should be watched/read by everyone. Here is what they came up with.

{% for rec in site.data.fiction %}
## Contributor: {{ rec["Contributor."] }}
<div class="home__column__main">
<div class="home__column" markdown=1>
**Work**. [{{ rec["Work."] }}]({{ rec["link"] }})

**Category**. {{ rec["Category."] }}

**Why watch this?** {{ rec["Why watch this?"] }}

{% if rec["Pitch"].size > 0 %}
{% assign id = "'" | append:rec["id"] | append:"'" %}
<span class="btn btn--danger" onclick="showpitch({{ id }})">Show More</span>
{% endif %}
</div>
<div class="home__column" markdown=1>
[![](/assets/images/fiction/{{ rec["image"] }})]({{ rec["link"] }})
</div>
</div>
<div class="fiction__pitch" id={{ id }} markdown=1>
<span class={{ rec["id"] }}><span>
{{ rec["Pitch"] }}
</div>
{% endfor %}

{% include footer/show_pitch.html %}
