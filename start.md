---
layout: landing
title: 소소의 작업실
permalink: /start/
description: AI로 그리고 손으로 다듬은 수채화 클립아트를 3일마다 무료로 드립니다. 만드는 법도, 파는 법도 전부 공개합니다.
image: /assets/brand/banner_blog.jpg
---

<section class="lp-hero">
  <div class="lp-wash lp-wash-a"></div>
  <div class="lp-wash lp-wash-b"></div>
  <div class="lp-hero-inner">
    <p class="lp-eyebrow">🌰 SOSO's Atelier</p>
    <h1 class="lp-h1">
      <span class="lp-word">수채화</span>
      <span class="lp-word">한 장으로</span>
      <span class="lp-word lp-accent">시작하는</span>
      <span class="lp-word">작은 작업실</span>
    </h1>
    <p class="lp-sub">
      AI로 그리고 사람이 한 장씩 다듬은 그림을 만듭니다.<br>
      그중 일부는 <strong>3일마다 무료로</strong> 나눠드려요.
    </p>
    <div class="lp-cta">
      <a class="lp-btn lp-btn-main" href="{{ '/freebies/' | relative_url }}">무료 클립아트 받기</a>
      <a class="lp-btn lp-btn-ghost" href="{{ '/posts/' | relative_url }}">어떻게 만드는지 보기</a>
    </div>
    <img class="lp-hero-soso" src="{{ '/assets/story/story_soso_wave.jpg' | relative_url }}" alt="인사하는 다람쥐 화가 소소">
  </div>
</section>

<section class="lp-stats">
  <div class="lp-stat"><span class="lp-num" data-to="110" data-suffix="+">0</span><span class="lp-stat-label">만든 파일</span></div>
  <div class="lp-stat"><span class="lp-num" data-to="4" data-suffix="종">0</span><span class="lp-stat-label">3일마다 무료 나눔</span></div>
  <div class="lp-stat"><span class="lp-num" data-to="100" data-suffix="%">0</span><span class="lp-stat-label">사람이 직접 검수</span></div>
</section>

<section class="lp-free">
  <p class="lp-kicker">이번 회차 무료 나눔</p>
  <h2 class="lp-h2">소소의 아침 책상</h2>
  <p class="lp-lead">판매 상품과 <strong>똑같은 공정</strong>으로 만든 투명 배경 PNG.<br>가입도 이메일도 필요 없습니다.</p>
  <div class="lp-free-grid">
    {% assign fb = "latte,sketchbook,acorns,tart" | split: "," %}
    {% assign fl = "라떼 한 잔,스케치북,도토리 삼형제,딸기 타르트" | split: "," %}
    {% for f in fb %}
    <figure class="lp-free-item">
      <img src="{{ '/assets/freebies/thumb/soso_' | append: f | append: '.jpg' | relative_url }}" alt="{{ fl[forloop.index0] }}" loading="lazy">
      <figcaption>{{ fl[forloop.index0] }}</figcaption>
    </figure>
    {% endfor %}
  </div>
  <a class="lp-btn lp-btn-main" href="{{ '/freebies/' | relative_url }}">지금 받으러 가기</a>
</section>

<section class="lp-how">
  <p class="lp-kicker">이렇게 만듭니다</p>
  <h2 class="lp-h2">AI는 시작일 뿐입니다</h2>
  <div class="lp-steps">
    <article class="lp-step">
      <span class="lp-step-n">01</span>
      <h3>스타일을 고정합니다</h3>
      <p>모든 그림에 같은 화풍 문장을 붙여 만듭니다. 몇 주에 걸쳐 그려도 한 사람이 그린 세트가 됩니다.</p>
    </article>
    <article class="lp-step">
      <span class="lp-step-n">02</span>
      <h3>한 장씩 눈으로 봅니다</h3>
      <p>문화 고증이 어긋나거나 이상한 소품이 섞이면 다시 그립니다. 60장 세트면 보통 5~10장을 다시 만듭니다.</p>
    </article>
    <article class="lp-step">
      <span class="lp-step-n">03</span>
      <h3>배경을 정성껏 지웁니다</h3>
      <p>그림 속 흰색은 살리고 바깥 배경만 투명하게. 이 후공정이 취미와 상품을 가릅니다.</p>
    </article>
  </div>
</section>


<section class="lp-video">
  <p class="lp-kicker">완성되는 과정</p>
  <h2 class="lp-h2">한 장씩 모여 하나가 됩니다</h2>
  <p class="lp-lead">낱장의 그림이 어떻게 쓰이는지, 7초면 보입니다.</p>
  <div class="lp-video-grid">
    {% assign vids = "ksc,kfr,kmk,kbp" | split: "," %}
    {% assign vnames = "K-스위츠 클립아트,수채화 프레임,한식 메뉴판 키트,비즈니스 페이지" | split: "," %}
    {% for v in vids %}
    <figure class="lp-vid">
      <video muted loop playsinline preload="none"
             poster="{{ '/assets/video/' | append: v | append: '_poster.jpg' | relative_url }}"
             aria-label="{{ vnames[forloop.index0] }} 미리보기 영상">
        <source src="{{ '/assets/video/' | append: v | append: '.mp4' | relative_url }}" type="video/mp4">
      </video>
      <figcaption>{{ vnames[forloop.index0] }}</figcaption>
    </figure>
    {% endfor %}
  </div>
</section>

<section class="lp-shop">
  <p class="lp-kicker">작업실 상품</p>
  <h2 class="lp-h2">무료로 써보고, 마음에 들면</h2>
  <p class="lp-lead">클립아트 62종, 메뉴판 템플릿, 한글 캘리그라피까지<br>같은 손으로 만든 컬렉션이 기다리고 있어요.</p>
  <div class="lp-shop-grid">
    {% assign top = site.data.products | slice: 0, 3 %}
    {% for p in top %}
    <a class="lp-card" href="{{ '/shop/' | relative_url }}#{{ p.id }}">
      <img src="{{ '/assets/shop/' | append: p.id | append: '.jpg' | relative_url }}" alt="{{ p.name }}" loading="lazy">
      <span class="lp-card-name">{{ p.name }}</span>
      <span class="lp-card-price">{{ p.price }}</span>
    </a>
    {% endfor %}
  </div>
  <a class="lp-btn lp-btn-ghost" href="{{ '/shop/' | relative_url }}">상품 전체 보기</a>
</section>

<section class="lp-last">
  <h2 class="lp-h2">오늘도 한 장, 스케치북을 채웁니다</h2>
  <p class="lp-lead">만드는 과정도 파는 과정도 숨기지 않고 적습니다.<br>실패한 것까지요.</p>
  <div class="lp-cta">
    <a class="lp-btn lp-btn-main" href="{{ '/freebies/' | relative_url }}">무료 클립아트 받기</a>
    <a class="lp-btn lp-btn-ghost" href="{{ '/posts/' | relative_url }}">작업 노트 읽기</a>
  </div>
</section>
