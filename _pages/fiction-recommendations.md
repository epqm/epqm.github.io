---
permalink: /fiction-recommendations/
classes: wide
title: "EPQM recommendations: Fiction"
excerpt: "Works of fiction that we feel everyone should experience at least once"
header:
    overlay_image: /assets/images/fiction/fiction_header.svg

---

We asked EPQM members to contribute a single work of fiction that they feel is remarkable and should be watched/read by everyone. Here is what they came up with.

{% for rec in site.data.fiction %}
<div class="home__column" markdown=1>
{% for field in rec limit:4 %}
**{{ field[0] }}** {% if field[0] != "Work." %}{{ field[1] }}{% else %}[{{ field[1] }}]({{ rec["link"] }}){% endif %}
{% endfor %}
<span class="btn btn--danger" onclick="showpitch('slal')">Show More</span>
</div>
<div class="home__column" markdown=1>
[![](/assets/images/fiction/{{ rec["image"] }})]({{ rec["link"] }})
</div>
{% if rec["Pitch"] %}
<div class="fiction__pitch" id="slal" markdown=1>
**Why watch this?** {{ rec["Pitch"] }}
</div>
{% endif %}
{% endfor %}
