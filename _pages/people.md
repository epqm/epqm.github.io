---
permalink: /people/
layout: single
title: Team members of EPQM
excerpt: Research scholars, masters students and alumni of the group

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
{%- if person["website"] != nil %}
Here's my [website.]({{ person["website"] }})
{% endif %}


{{ person["work"] }}
{: class="people__work" }

{% if person["graduated"] != nil %}
Graduated in {{ person["graduated"] }}
{% endif %}

</div>
{% endfor %}
{% endfor %}
