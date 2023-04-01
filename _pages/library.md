---
permalink: /epqmlibrary/
layout: splash
title: "EPQM Library"
excerpt: "Database and maintainence system for our books"
header:
    overlay_image: /assets/images/seminars/seminars_header.svg

---

<table id="EpqmLibraryTable" class="sortable">
<thead>
<td class="epqm__table__center">Id</td>
<td>Book</td>
<td>Authors</td>
<td class="epqm__table__center">Spot</td>
<td class="epqm__table__center">Status</td>
</thead>
{% for entry in site.data.EPQMLibrary %}
<tr id="epqm__library__{{ forloop.index }}">
<td class="epqm__table__center">{{ forloop.index }}</td><td><strong>{{ entry["title"] }}</strong></td><td>{{ entry["authors"] }}</td>
<td class="epqm__table__center">{{ entry["spot"] }}</td>
<td class="epqm__table__center">
<i class="far fa-heart" onclick="borrowBook({{ forloop.index }})" style="display:{% if entry["status"] == nil %}block{% else %}none{% endif %}"></i>
<i class="fas fa-heart" onclick="toggleInfo({{ forloop.index }})" style="display:{% if entry["status"] == nil %}none{% else %}block{% endif %}"></i>
<div style="display: none;" onclick="releaseBook({{ forloop.index }})" id="book__info__{{ forloop.index }}">{{ entry["status"] }}</div>
</td>
</tr>
{% endfor %}
</table>

{% include library.html %}
