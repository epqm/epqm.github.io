---
permalink: /people/
layout: single
title: "Team members of EPQM: the past and the present"
excerpt: Research scholars, masters students and alumni of the group
header:
    image: /assets/images/people.svg

---

{% for class in site.data.people %}

## {{ class[0] }}

{% for person in class[1] %}

<div class="people__desc" markdown=1>

![]({{ person["img_path"] }}){: class="people__img" }
**{{ person["name"] }}**

{% if person["designation"] != nil %}
{{ person["designation"] }},
{% endif %}
Contact me at [{{ person["email"] }}](mailto:{{ person["email"] }}).

{{ person["work"] }}
{: class="people__work" }

</div>
{% endfor %}
{% endfor %}
