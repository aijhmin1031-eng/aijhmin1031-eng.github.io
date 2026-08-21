/* 소소의 작업실 — 등장·스크롤 인터랙션
   원칙: 브랜드 비디오와 같은 "빌드업 팝인" 문법, 과하지 않게, 접근성 존중 */
(function () {
  'use strict';

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var root = document.documentElement;
  root.classList.add('js-anim');
  if (reduce) { root.classList.add('reduce-motion'); return; }

  /* 1) 스크롤 등장 — 화면에 들어오면 한 번만 재생 */
  var SELECTOR = [
    '.story-row', '.post-card', '.fb-item', '.shop-cta', '.freebie-callout',
    '.starter-box', '.drop-head', '.mini-cta', '.product', '.buy-note', '.post-content > h2',
    '.post-content > h3', '.post-content > p', '.post-content > ul',
    '.post-content > ol', '.post-content > table', '.post-content > blockquote',
    '.post-content > p > img', '.latest-heading'
  ].join(',');

  var targets = Array.prototype.slice.call(document.querySelectorAll(SELECTOR));
  targets.forEach(function (el) { el.classList.add('reveal'); });

  /* 그리드 안의 형제들은 순차 지연 (비디오의 0.19s 간격 감성) */
  function stagger(containerSel, itemSel, step) {
    Array.prototype.forEach.call(document.querySelectorAll(containerSel), function (box) {
      Array.prototype.forEach.call(box.querySelectorAll(itemSel), function (el, i) {
        el.style.setProperty('--d', (i * step) + 'ms');
      });
    });
  }
  stagger('.post-cards', '.post-card', 90);
  stagger('.freebie-grid', '.fb-item', 110);
  stagger('.story', '.story-row', 60);

  if (!('IntersectionObserver' in window)) {
    targets.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    targets.forEach(function (el) { io.observe(el); });

    /* 첫 화면 + 빠른 스크롤로 지나친 요소를 놓치지 않는 스윕 폴백 */
    var sweep = function () {
      targets.forEach(function (el) {
        if (el.classList.contains('in')) return;
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight * 0.96) { el.classList.add('in'); io.unobserve(el); }
      });
    };
    requestAnimationFrame(sweep);
    var sweepTick = null;
    window.addEventListener('scroll', function () {
      if (sweepTick) return;
      sweepTick = setTimeout(function () { sweepTick = null; sweep(); }, 120);
    }, { passive: true });
    window.addEventListener('load', sweep);
  }

  /* 2) 글 읽기 진행 막대 */
  var article = document.querySelector('.post-content');
  if (article) {
    var bar = document.createElement('div');
    bar.className = 'read-bar';
    bar.innerHTML = '<span></span>';
    document.body.appendChild(bar);
    var fill = bar.firstChild;
    var tick = function () {
      var top = article.offsetTop;
      var h = article.offsetHeight - window.innerHeight;
      var p = h > 0 ? (window.scrollY - top) / h : 0;
      fill.style.transform = 'scaleX(' + Math.min(1, Math.max(0, p)) + ')';
    };
    tick();
    window.addEventListener('scroll', tick, { passive: true });
    window.addEventListener('resize', tick);
  }

  /* 3) 스크롤하면 헤더에 그림자 */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('scrolled', window.scrollY > 12);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* 4) 라이트박스 열림/닫힘 부드럽게 + ESC로 닫기 */
  window.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && location.hash.indexOf('#view-') === 0) {
      history.pushState('', document.title, location.pathname + location.search);
    }
  });
})();

/* ── Pinterest 저장 버튼 — 본문 이미지 위에 얹기 ───────────────── */
(function () {
  'use strict';
  var imgs = document.querySelectorAll('.post-content img, .home .story-row img, .product-img img');
  if (!imgs.length) return;
  var pageUrl = location.href;

  Array.prototype.forEach.call(imgs, function (img) {
    if (img.closest('.pin-wrap') || img.closest('.pc-thumb') || img.closest('.shop-cta')) return;
    var src = img.currentSrc || img.src;
    if (!src) return;

    var wrap = document.createElement('span');
    wrap.className = 'pin-wrap';
    img.parentNode.insertBefore(wrap, img);
    wrap.appendChild(img);

    var a = document.createElement('a');
    a.className = 'pin-save';
    a.target = '_blank';
    a.rel = 'noopener';
    a.title = 'Pinterest에 저장';
    a.setAttribute('aria-label', 'Pinterest에 저장');
    a.href = 'https://www.pinterest.com/pin/create/button/?url=' + encodeURIComponent(pageUrl) +
             '&media=' + encodeURIComponent(src) +
             '&description=' + encodeURIComponent(img.alt || document.title);
    a.innerHTML = '<svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true">' +
      '<path fill="currentColor" d="M12 0C5.4 0 0 5.4 0 12c0 5.1 3.2 9.4 7.6 11.2-.1-.9-.2-2.4 0-3.4l1.4-5.9s-.3-.7-.3-1.8c0-1.7 1-2.9 2.2-2.9 1 0 1.5.8 1.5 1.7 0 1-.7 2.6-1 4.1-.3 1.2.6 2.2 1.8 2.2 2.2 0 3.8-2.3 3.8-5.6 0-2.9-2.1-5-5.1-5-3.5 0-5.5 2.6-5.5 5.3 0 1 .4 2.2.9 2.8.1.1.1.2.1.3l-.3 1.3c0 .2-.2.3-.4.2-1.5-.7-2.4-2.9-2.4-4.7 0-3.8 2.8-7.4 8-7.4 4.2 0 7.5 3 7.5 7 0 4.2-2.6 7.5-6.3 7.5-1.2 0-2.4-.6-2.8-1.4l-.8 2.9c-.3 1.1-1 2.5-1.6 3.4 1.2.4 2.4.6 3.7.6 6.6 0 12-5.4 12-12S18.6 0 12 0z"/></svg>' +
      '<span>저장</span>';
    wrap.appendChild(a);
  });
})();

/* ── 글 모아보기: 검색 + 카테고리 필터 ───────────────────────── */
(function () {
  'use strict';
  var root = document.querySelector('.post-index');
  if (!root) return;

  var q = document.getElementById('pi-q');
  var countEl = document.getElementById('pi-count');
  var emptyEl = document.getElementById('pi-empty');
  var chips = [].slice.call(root.querySelectorAll('.pi-chip'));
  var items = [].slice.call(root.querySelectorAll('.pi-item'));
  var years = [].slice.call(root.querySelectorAll('.pi-year'));
  var cat = '';

  function norm(s) { return (s || '').toLowerCase().replace(/\s+/g, ' '); }

  function apply() {
    var term = norm(q ? q.value : '');
    var shown = 0;
    items.forEach(function (li) {
      var okCat = !cat || (' ' + li.dataset.cat + ' ').indexOf(' ' + cat + ' ') > -1;
      var okTerm = !term || norm(li.dataset.text).indexOf(term) > -1;
      var on = okCat && okTerm;
      li.hidden = !on;
      if (on) shown++;
    });
    years.forEach(function (sec) {
      sec.hidden = !sec.querySelector('.pi-item:not([hidden])');
    });
    if (countEl) countEl.textContent = shown + '편';
    if (emptyEl) emptyEl.hidden = shown !== 0;
  }

  if (q) {
    var t = null;
    q.addEventListener('input', function () {
      clearTimeout(t); t = setTimeout(apply, 120);
    });
  }
  chips.forEach(function (b) {
    b.addEventListener('click', function () {
      chips.forEach(function (x) { x.classList.remove('is-on'); });
      b.classList.add('is-on');
      cat = b.dataset.cat || '';
      apply();
    });
  });

  /* 주소에 #카테고리 가 있으면 그 카테고리로 시작 */
  if (location.hash.length > 1) {
    var want = decodeURIComponent(location.hash.slice(1));
    var hit = chips.filter(function (b) { return b.dataset.cat === want; })[0];
    if (hit) hit.click();
  }
  apply();
})();

/* ── 글 목차 (소제목 3개 이상일 때만) ─────────────────────────── */
(function () {
  'use strict';
  var content = document.querySelector('.post-content');
  if (!content) return;
  var hs = [].slice.call(content.querySelectorAll('h2, h3'));
  if (hs.length < 3) return;

  var box = document.createElement('nav');
  box.className = 'toc';
  var html = '<button class="toc-toggle" aria-expanded="true">📑 이 글의 목차</button><ol class="toc-list">';
  hs.forEach(function (h, i) {
    if (!h.id) h.id = 'sec-' + i;
    html += '<li class="toc-' + h.tagName.toLowerCase() + '"><a href="#' + h.id + '">' +
            h.textContent.trim() + '</a></li>';
  });
  box.innerHTML = html + '</ol>';
  content.insertBefore(box, content.firstChild);

  var btn = box.querySelector('.toc-toggle');
  btn.addEventListener('click', function () {
    var open = box.classList.toggle('collapsed');
    btn.setAttribute('aria-expanded', String(!open));
  });

  /* 읽는 위치 표시 */
  var links = [].slice.call(box.querySelectorAll('a'));
  if ('IntersectionObserver' in window) {
    var spy = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (a) {
          a.classList.toggle('on', a.getAttribute('href') === '#' + e.target.id);
        });
      });
    }, { rootMargin: '-10% 0px -80% 0px' });
    hs.forEach(function (h) { spy.observe(h); });
  }
})();

/* ── 스티키 헤더: 스크롤하면 압축 + 글 제목 표시 ──────────────── */
(function () {
  'use strict';
  var header = document.querySelector('.site-header');
  if (!header) return;
  var wrap = header.querySelector('.wrapper');
  var h1 = document.querySelector('.post-title');

  var titleEl = null;
  if (h1 && wrap) {
    titleEl = document.createElement('span');
    titleEl.className = 'header-post-title';
    titleEl.textContent = h1.textContent.trim();
    wrap.insertBefore(titleEl, wrap.querySelector('.site-nav'));
  }

  var lastCompact = null;
  function onScroll() {
    var y = window.scrollY || document.documentElement.scrollTop;
    var compact = y > 120;
    if (compact !== lastCompact) {
      header.classList.toggle('compact', compact);
      lastCompact = compact;
    }
    if (titleEl) {
      var past = h1.getBoundingClientRect().bottom < 56;
      header.classList.toggle('show-title', past);
    }
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
})();
