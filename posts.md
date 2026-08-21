---
layout: page
title: 글 모아보기
permalink: /posts/
---

<div class="post-index">
  <div class="pi-search">
    <input type="search" id="pi-q" placeholder="🔍  제목·내용으로 검색해 보세요" autocomplete="off" aria-label="글 검색">
    <p class="pi-count" id="pi-count"></p>
  </div>

  {%- assign cats = site.categories | sort -%}
  <div class="pi-cats">
    <button class="pi-chip is-on" data-cat="">전체 <span>{{ site.posts.size }}</span></button>
    {%- for c in cats -%}
    <button class="pi-chip" data-cat="{{ c[0] }}">{{ c[0] }} <span>{{ c[1].size }}</span></button>
    {%- endfor -%}
  </div>

  <p class="pi-empty" id="pi-empty" hidden>찾으시는 글이 없습니다. 다른 검색어로 시도해 보세요.</p>

  {%- assign posts_by_year = site.posts | group_by_exp: "p", "p.date | date: '%Y'" -%}
  {%- for year in posts_by_year -%}
  <section class="pi-year" data-year="{{ year.name }}">
    <h2 class="pi-year-title">{{ year.name }}년</h2>
    <ul class="pi-list">
      {%- for post in year.items -%}
      <li class="pi-item"
          data-cat="{{ post.categories | join: ' ' }}"
          data-text="{{ post.title | append: ' ' | append: post.content | strip_html | truncate: 400 | escape }}">
        <a href="{{ post.url | relative_url }}">
          {%- if post.image -%}
          <span class="pi-thumb"><img src="{{ post.image | relative_url }}" alt="" loading="lazy"></span>
          {%- endif -%}
          <span class="pi-body">
            {%- if post.categories.size > 0 -%}<span class="pc-cat">{{ post.categories | first }}</span>{%- endif -%}
            <span class="pi-title">{{ post.title | escape }}</span>
            <span class="pi-date">{{ post.date | date: "%m월 %d일" }}</span>
          </span>
        </a>
      </li>
      {%- endfor -%}
    </ul>
  </section>
  {%- endfor -%}
</div>
