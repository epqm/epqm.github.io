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
<div class="people-head-name"> Siddhartha Lal </div>
PhD (IISc), <a href="https://www.iiserkol.ac.in/web/en/people/faculty/dps/slal/">Associate Professor, IISER Kolkata</a><br><br>
<p>Interested in strongly correlated electronic systems, fermionic<br>
 criticality, low-dimensional quantum systems, etc.</p>
Contact me at <a href="mailto:slal@iiserkol.ac.in">slal@iiserkol.ac.in</a><br>
</div>
</div>

## Research scholars

<div class="people-head">
{% for person in site.data.people.scholars %}

{% assign mod = forloop.index | modulo: 2 %}
{% if mod == 1 %}
<div style="width:45%;float:left;text-align:justify;margin-bottom:2em;" markdown=1>
{% else %}
<div style="width:45%;float:right;text-align:justify;margin-bottom:2em;" markdown=1>
{% endif %}
<div style="width:200px;margin: auto;">
<img src="{{ person["img_path"] }}">
</div>
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
<div style="width:45%;float:left;text-align:justify;margin-bottom:2em;" markdown=1>
{% else %}
<div style="width:45%;float:right;text-align:justify;margin-bottom:2em;" markdown=1>
{% endif %}
**{{ person["name"] }}**<br>
[{{ person["email"] }}](mailto:{{ person["email"] }})

{{ person["education"] }}

{{ person["research"] }}

</div>
{% endfor %}
</div>
