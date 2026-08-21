---
layout: page
title: 무료 나눔
permalink: /freebies/
---

## 🎁 3일마다 수채화 클립아트 4종을 무료로 드립니다

판매용 상품과 **똑같은 공정**(수채화 생성 → 배경 투명화 → 전수 검수)으로 만든
고해상도 투명 PNG입니다. 회원가입도, 이메일 등록도 필요 없어요.
지난 회차도 계속 받을 수 있으니 편하게 가져가세요.

<p class="drop-next">📅 다음 공개 예정일 — <strong>{{ site.next_drop }}</strong> · 새 팩은 이 페이지 맨 위에 올라옵니다</p>

{% assign packs = site.data.freebies | sort: "vol" | reverse %}
{% for pack in packs %}
<div class="drop-head">
  <span class="drop-vol">Vol.{{ pack.vol }}</span>
  <span class="drop-title">{{ pack.title }}</span>
  <span class="drop-date">{{ pack.date | date: "%Y년 %m월 %d일" }} 공개</span>
</div>
{% if pack.note %}<p class="drop-note">{{ pack.note }}</p>{% endif %}

<div class="freebie-grid">
{% for it in pack.items %}
  <div class="fb-item">
    <a class="fb-preview" href="#view-{{ it.file }}">
      <img src="{{ '/assets/freebies/thumb/soso_' | append: it.file | append: '.jpg' | relative_url }}"
           alt="{{ it.label }} 수채화 클립아트" loading="lazy">
      <span class="fb-zoom">🔍 크게 보기</span>
    </a>
    <p class="fb-name">{{ it.label }}</p>
    <a class="fb-dl" href="{{ '/assets/freebies/png/soso_' | append: it.file | append: '.png' | relative_url }}" download>⬇ PNG 받기</a>
  </div>
{% endfor %}
</div>

<p class="fb-all">4종을 한 번에 받고 싶다면 → <a href="{{ pack.zip | relative_url }}">Vol.{{ pack.vol }} 전체 ZIP 받기</a></p>
{% endfor %}

{% for pack in packs %}{% for it in pack.items %}
<div class="fb-lightbox" id="view-{{ it.file }}">
  <a class="fb-close" href="#">✕ 닫기</a>
  <img src="{{ '/assets/freebies/thumb/soso_' | append: it.file | append: '_lg.jpg' | relative_url }}" alt="{{ it.label }} 크게 보기">
  <a class="fb-dl" href="{{ '/assets/freebies/png/soso_' | append: it.file | append: '.png' | relative_url }}" download>⬇ 원본 PNG 받기</a>
</div>
{% endfor %}{% endfor %}

### 파일 정보

- **투명 배경 PNG**, 3000×3000px 고해상도 (파일당 3~5MB)
- 폰에서 받으면 갤러리에, PC에서 받으면 다운로드 폴더에 저장됩니다

### 사용 범위

- ✅ 개인 프로젝트, 다이어리 꾸미기, 소상공인 홍보물 등 자유롭게 사용
- ❌ 파일 자체의 재판매·재배포(무료 배포 포함)는 안 됩니다
- 이미지들은 AI 생성 후 수작업 검수·후처리를 거쳤습니다

{% include shop-cta.html %}
