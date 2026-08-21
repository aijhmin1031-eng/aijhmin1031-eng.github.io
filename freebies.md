---
layout: page
title: 무료 나눔
permalink: /freebies/
---

## 🎁 소소의 아침 책상 — 무료 수채화 클립아트 5종

판매용 상품과 **똑같은 공정**(수채화 생성 → 배경 투명화 → 전수 검수)으로 만든
고해상도 투명 PNG입니다. 회원가입도, 이메일 등록도 필요 없어요.
마음에 드는 것만 골라 받으셔도 됩니다.

<div class="freebie-grid">
{% assign items = "latte,sketchbook,acorns,tart,blossom" | split: "," %}
{% assign labels = "라떼 한 잔,스케치북,도토리 삼형제,딸기 타르트,벚꽃 가지" | split: "," %}
{% for it in items %}
  <div class="fb-item">
    <a class="fb-preview" href="#view-{{ it }}">
      <img src="{{ '/assets/freebies/thumb/soso_' | append: it | append: '.jpg' | relative_url }}"
           alt="{{ labels[forloop.index0] }} 수채화 클립아트" loading="lazy">
      <span class="fb-zoom">🔍 크게 보기</span>
    </a>
    <p class="fb-name">{{ labels[forloop.index0] }}</p>
    <a class="fb-dl" href="{{ '/assets/freebies/png/soso_' | append: it | append: '.png' | relative_url }}" download>⬇ PNG 받기</a>
  </div>
{% endfor %}
</div>

{% for it in items %}
<div class="fb-lightbox" id="view-{{ it }}">
  <a class="fb-close" href="#">✕ 닫기</a>
  <img src="{{ '/assets/freebies/thumb/soso_' | append: it | append: '_lg.jpg' | relative_url }}"
       alt="{{ labels[forloop.index0] }} 크게 보기">
  <a class="fb-dl" href="{{ '/assets/freebies/png/soso_' | append: it | append: '.png' | relative_url }}" download>⬇ 원본 PNG 받기</a>
</div>
{% endfor %}

<p class="fb-all">
  5종을 한 번에 받고 싶다면 →
  <a href="{{ "/assets/freebies/soso_desk_freebie_pack.zip" | relative_url }}">전체 ZIP 다운로드 (19MB)</a>
</p>

### 파일 정보

- **투명 배경 PNG**, 3000×3000px 고해상도 (파일당 3~5MB)
- 폰에서 받으면 갤러리에, PC에서 받으면 다운로드 폴더에 저장됩니다

### 사용 범위

- ✅ 개인 프로젝트, 다이어리 꾸미기, 소상공인 홍보물 등 자유롭게 사용
- ❌ 파일 자체의 재판매·재배포(무료 배포 포함)는 안 됩니다
- 이미지들은 AI 생성 후 수작업 검수·후처리를 거쳤습니다

### 전체 세트가 필요하다면

이 5종은 저희 수채화 컬렉션의 맛보기입니다. 62종 풀세트와 메뉴판 템플릿 등은
[SOSO 상점](https://payhip.com/SosotoryStudio)에서 만나보실 수 있어요. 🌰

---

_새 무료 팩은 **3일마다** 올라옵니다. 다음 팩은 "홈카페 티타임"이에요._
