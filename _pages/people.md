---
permalink: /people/
layout: single
title: "People in EPQM"

---

<br>
<div class="people-head">
<div class="people-head-img">
<img src="/assets/images/people/slal.jpg">
</div>
<div class="people-head-text">
<div class="people-head-name"> Siddhartha Lal</div>
PhD (IISc), <a href="https://www.iiserkol.ac.in/web/en/people/faculty/dps/slal/">Associate Professor, IISER Kolkata</a><br><br>
<p>Interested in strongly correlated electrons, fermionic criticality, low-dim. quantum systems, etc.</p>
Contact me at <a href="mailto:slal@iiserkol.ac.in">slal@iiserkol.ac.in</a><br>
</div>
</div>

## Research scholars

<div class="people-head">
{% for person in site.data.people.scholars %}

{% assign mod = forloop.index | modulo: 2 %}
{% if mod == 1 %}
<div class="people-text-left" markdown=1>
{% else %}
<div class="people-text-right" markdown=1>
{% endif %}

<img src="{{ person["img_path"] }}" class="people-img">

**{{ person["name"] }}**<br>
[{{ person["email"] }}](mailto:{{ person["email"] }})

{{ person["education"] }}

{{ person["research"] }}

</div>
{% endfor %}
</div>

## Masters students

<div class="people-head">
{% for person in site.data.people.masters %}

{% assign mod = forloop.index | modulo: 2 %}
{% if mod == 1 %}
<div class="people-text-left" markdown=1>
{% else %}
<div class="people-text-right" markdown=1>
{% endif %}
**{{ person["name"] }}**<br>
[{{ person["email"] }}](mailto:{{ person["email"] }})

{{ person["education"] }}

{{ person["research"] }}

</div>
{% endfor %}
</div>
