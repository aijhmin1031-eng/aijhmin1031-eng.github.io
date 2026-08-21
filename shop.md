---
layout: page
title: 상품
permalink: /shop/
faq:
  - q: 상업적으로 써도 되나요?
    a: 네. 개인 프로젝트와 소상공인 사업 용도로 자유롭게 쓰실 수 있습니다. 다만 파일 자체를 되팔거나 재배포하는 것은 안 됩니다.
  - q: 어떤 프로그램이 필요한가요?
    a: PNG는 캔바·워드·파워포인트·프로크리에이트 등 대부분의 도구에서 바로 열립니다. SVG는 확대해도 깨지지 않는 형식이라 커팅기나 일러스트레이터에서 씁니다.
  - q: 결제는 어떻게 하나요?
    a: 상품 페이지는 해외 판매 플랫폼에 있어 영문으로 열립니다. PayPal 또는 해외결제 가능한 카드로 결제하시면 되고, 결제 직후 다운로드 링크가 바로 나옵니다.
  - q: 무료로 먼저 써볼 수 있나요?
    a: 네. 무료 나눔 페이지에서 판매 상품과 같은 공정으로 만든 수채화 클립아트를 3일마다 4종씩 무료로 드립니다.
---

## 🌰 소소의 작업실 상품

AI로 그리고 **한 장씩 손으로 검수해서** 만든 수채화 디지털 파일입니다.
전부 내려받아 바로 쓰는 상품이라 배송이 없고, 결제하면 즉시 다운로드됩니다.

<div class="buy-note">
  <strong>결제 안내</strong> — 상품 페이지는 해외 판매 플랫폼(Payhip)에 있어 <b>영문</b>으로 열립니다.
  <b>PayPal 또는 해외결제 가능한 카드</b>로 결제하시면 되고, 결제 직후 다운로드 링크가 바로 나옵니다.
  가격은 달러(USD) 기준이라 카드사 환율로 원화 청구됩니다.
</div>

{% for p in site.data.products %}
<div class="product" id="{{ p.id }}">
  <a class="product-img" href="{{ p.url }}" target="_blank" rel="noopener">
    <img src="{{ '/assets/shop/' | append: p.id | append: '.jpg' | relative_url }}" alt="{{ p.name }} 미리보기" loading="lazy">
  </a>
  <div class="product-body">
    {% if p.badge %}<span class="product-badge">{{ p.badge }}</span>{% endif %}
    <h3 class="product-name">{{ p.name }}</h3>
    <p class="product-en">{{ p.en }}</p>
    <p class="product-desc">{{ p.desc }}</p>
    <p class="product-detail">{{ p.detail }}</p>
    <p class="product-buy">
      <span class="product-price">{{ p.price }}</span>
      <a class="product-btn" href="{{ p.url }}" target="_blank" rel="noopener">상점에서 보기 →</a>
    </p>
  </div>
</div>
{% endfor %}

### 자주 묻는 질문

**Q. 상업적으로 써도 되나요?**
네. 개인 프로젝트와 소상공인 사업 용도로 자유롭게 쓰실 수 있습니다.
다만 **파일 자체를 되팔거나 재배포하는 것**은 안 됩니다.

**Q. 어떤 프로그램이 필요한가요?**
PNG는 캔바·워드·파워포인트·프로크리에이트 등 대부분의 도구에서 바로 열립니다.
SVG는 확대해도 깨지지 않는 형식이라 커팅기(크리컷 등)나 일러스트레이터에서 씁니다.

**Q. 결제가 어렵습니다.**
[문의 페이지]({{ "/contact/" | relative_url }})로 연락 주시면 도와드리겠습니다.

**Q. 무료로 먼저 써볼 수 있나요?**
네, [무료 나눔]({{ "/freebies/" | relative_url }})에서 판매 상품과 같은 공정으로 만든
클립아트를 3일마다 4종씩 드립니다.

---

_이미지는 AI 도구로 생성한 뒤 사람이 전수 검수·후처리한 결과물입니다._
