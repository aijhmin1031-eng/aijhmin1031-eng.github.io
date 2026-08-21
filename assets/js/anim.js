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
