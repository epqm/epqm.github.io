---
permalink: /people/
layout: single
title: "Team members of EPQM: the past and the present"
excerpt: Research scholars, masters students and alumni of the group
header:
    overlay_image: ../assets/images/blob-haikei.svg

---

## Group leader
{% assign head = site.data.people.head %}

<div class="people__desc" markdown=1>

![](/assets/images/people/slal.jpg){: class="people__img" }

**{{ head["name"] }}**

<a href="https://www.iiserkol.ac.in/web/en/people/faculty/dps/slal/">{{ head["designation"] }}</a><br><br>
{{ head["interests"] }}<br><br>
Contact me at <a href="mailto:slal@iiserkol.ac.in">{{ head["email"] }}</a><br>
</div>

## Research scholars

{% for person in site.data.people.current %}
<div class="people__desc" markdown=1>

![]({{ person["img_path"] }}){: class="people__img" }
**{{ person["name"] }}**

{% if person["designation"] == nil %}
    {{ person["designation"] }},
{% endif %}
[{{ person["email"] }}](mailto:{{ person["email"] }})

{{ person["work"] }}

</div>
{% endfor %}

## Alumni

{% for person in site.data.people.alumni %}
<div class="people__desc" markdown=1>

![]({{ person["img_path"] }}){: class="people__img" }
**{{ person["name"] }}**

[{{ person["email"] }}](mailto:{{ person["email"] }})

{{ person["work"] }}

</div>
{% endfor %}
