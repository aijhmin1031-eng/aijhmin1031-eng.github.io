---
layout: page
title: English
permalink: /en/
---

## Posts in English

Hands-on notes on digital side hustles — selling digital design files,
using AI tools in production, and setting up cross-border payouts.

{% assign en_posts = site.posts | where: "lang", "en" %}
<ul>
  {% for post in en_posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      — {{ post.date | date: "%Y-%m-%d" }}
    </li>
  {% endfor %}
</ul>
