---
permalink: /about/
layout: single
title: "All About EPQM"
toc: true
toc_sticky: true
excerpt: "EPQM is a research group at IISER Kolkata lead by Dr. **Siddhartha Lal** in the Department of Physical Sciences at IISER Kolkata."
gallery:
    - image_path: /assets/images/about/epqm_logo.svg
      url: /
    - url: https://www.iiserkol.ac.in/web/en/
      image_path: /assets/images/about/IISER-K_Logo.svg
    - url: https://physics.iiserkol.ac.in/
      image_path: /assets/images/about/dps-logo.svg
header:
    overlay_image: /assets/images/about/about_header.jpg
    caption: "[Source](https://phdcomics.com/comics.php?f=1760)"
    actions:
    - label: Publications
      url: /publications/
    - label: People
      url: /about/#people
    - label: Openings
      url: /about/#openings

---

# What is EPQM?

**EPQM** (Emergent Phenomena in Quantum Matter) is a research group at IISER Kolkata lead by Dr. **Siddhartha Lal** in the Department of Physical Sciences at the Indian Institute of Science Education and Research (IISER) Kolkata, India. We engage in theoretical research on various topics in **quantum condensed matter physics**, ranging from strongly-correlated electronic systems and quantum magnetism to topological phases of matter and non-Fermi liquids.

Our work often involves the development of non-perturbative methods like a novel **renormalisation group method**, twist operator-based techniques and momentum-space entanglement renormalisation group approaches. Many of our results derive ideas from **topology**, number theory, graph theory, machine learning, quantum information theory and non-linear dynamics.

For more information, please take a look at our [research work](/research/) and our [publications](/research/#publications).

# Group members
{:id="people"}

{% for class in site.data.people %}

## {{ class[0] }}

{% include feature_row_people.html %}

{% endfor %}

{% include gallery %}

# Contact Details

The easiest way to reach out is to send an [email](mailto:slal@iiserkol.ac.in).

# Openings

There are no open positions in the group at the moment.

**EPQM,<br>
Department of Physical Sciences,<br>
Research Complex, IISER Kolkata,<br>
Mohanpur-741246, West Bengal, India.**
