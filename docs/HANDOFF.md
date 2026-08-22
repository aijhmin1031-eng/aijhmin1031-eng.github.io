# 🔄 인수인계 — 소소의 작업실 블로그 (2026-08-22 기준)

> **이어받는 AI에게.** 이 문서 하나로 이 블로그를 혼자 운영할 수 있게 썼다.
> 읽는 순서: ① 이 문서 ② `../CLAUDE.md`(발행 공정·절대 규칙) ③ `운영계획.md`(전략·수익화)
> ④ `글감백로그_AI시리즈.md` / `무료나눔_테마백로그.md`(다음에 쓸 것들).
> 이 폴더(`docs/`)는 `_config.yml`의 `exclude`에 있어 **공개 사이트에 노출되지 않는다.**

---

## 1. 이게 뭔가 — 30초 요약

| 항목 | 값 |
|---|---|
| 사이트 | https://aijhmin1031-eng.github.io/ |
| repo | `aijhmin1031-eng/aijhmin1031-eng.github.io` (Public) |
| 호스팅 | GitHub Pages + Jekyll(minima 테마). **main 푸시 → 1~2분 후 자동 배포** |
| 브랜드 | 소소의 작업실 (SOSO's Atelier), 마스코트 다람쥐 화가 "소소" |
| 언어 | **한국어 전용** (영어판은 `_unpublished_en/`에 보관 — 빌드 제외) |
| 주제 | AI로 디지털 상품을 만들어 파는 1인 작업실의 실전 기록 |
| 목적 | ① Google AdSense 수익화 ② Payhip 상점(SosotoriStudio) 유입 |
| 공개 이메일 | aijhmin1031@gmail.com (contact 페이지) |
| 자동화 | 매일 07:00 KST 글 1편 / 3일마다 07:30 KST 무료나눔 드랍 (§6) |

**말투·태도**: 사용자(선배님)에게는 한국어 존댓말. 글은 "직접 해봤다" 톤 —
과장·수익 보장 금지, 숫자는 실측만. 이건 취향이 아니라 AdSense 심사 대비 원칙이다.

---

## 2. 사이트 구조 지도

```
_config.yml            사이트 설정. timezone·permalink·exclude·next_drop — §7 함정 참조
_data/products.yml     상점 상품 9종 (shop.md가 이 데이터로 렌더링)
_data/freebies.yml     무료나눔 회차 기록 (freebies.md가 이 데이터로 렌더링)
_posts/                발행된 글 (YYYY-MM-DD-슬러그.md)
_unpublished_en/       영어판 보관 — 빌드 제외, 지우지 말 것
_layouts/
  home.html            홈: 스토리 4블록 → "처음 오셨다면" → 작업 노트 카드
  post.html            글: 본문 → 공유 → 상점 CTA → 이전/다음 → 미니 CTA
  landing.html         /start/ 랜딩 (카운트업·비디오·임팩트 구성)
_includes/
  head.html            웹폰트·파비콘·anim.js·FAQ 스키마 로드
  header.html          ⚠️ 모바일 햄버거(nav-trigger) 구조 — 지우면 폰에서 메뉴가 콘텐츠를 덮는다
  footer.html / share.html / shop-cta.html / post-nav.html / faq-schema.html
index.md  posts.md  shop.md  freebies.md  about.md  contact.md  privacy.md  start.md
assets/
  main.scss (807줄)    minima 오버라이드 — 막대 제거 + 한글 타이포 (§5)
  js/anim.js           인터랙션 7블록 (§4)
  brand/               배너·프로필·파비콘 4종·상점 삽화
  shop/                상품 커버 9장 (id.jpg — products.yml의 id와 일치)
  video/               홍보 mp4 4편 + 포스터 (ksc·kfr·kmk·kbp, 총 608KB)
  og/                  글별 공유 카드 1200×630
  freebies/png|thumb/  무료나눔 원본 투명 PNG + 미리보기
  story/               홈 스토리 삽화
docs/                  내부 문서 (이 파일 포함) — 빌드 제외
scripts/               생성·검증 도구 (§3) — 빌드 제외
google*.html / naver*.html   검색엔진 소유확인 파일 — 삭제 금지
```

### front matter 규약 (외우면 좋다)

```yaml
---
layout: post
title: "제목"
date: 2026-08-22 06:30:00 +0900   # ⚠️ 반드시 현재보다 과거. 미래면 빌드에서 제외된다
lang: ko
image: /assets/og/슬러그.jpg       # OG 공유 카드 1200×630 (카톡·X 미리보기용)
thumb: /assets/슬러그.jpg          # 히어로 = 목록 카드 썸네일
categories: AI부업                 # 또는 무료나눔·시작가이드
starter: true                      # 입문용 글만! 홈 "처음 오셨다면"에 노출
starter_order: 2                   # starter일 때 정렬 순서
faq:                               # 있으면 FAQPage 구조화 데이터 자동 생성 (검색 노출 유리)
  - q: 질문
    a: 답변
---
```

`image`와 `thumb`를 혼동하지 말 것 — `image`는 공유 카드(글자 박힌 1200×630),
`thumb`는 히어로 삽화. 둘을 바꿔 넣으면 카톡 미리보기에서 제목이 안 보인다.

---

## 3. 도구 — `scripts/` (repo 커밋됨, 빌드 제외)

| 스크립트 | 용도 | 사용법 |
|---|---|---|
| **check_build.py** | **푸시 전 필수.** `_data/*.yml`·`_config.yml`·모든 front matter YAML 검증 | `python3 scripts/check_build.py` (repo 루트에서) |
| hero_gen.py | 히어로 삽화 (Pollo GPT Image 2, 3:2, 1200px JPEG). 수채 STYLE 접미사 고정 | `POLLO_API_KEY=... python3 scripts/hero_gen.py "<영문 장면>" assets/슬러그.jpg` |
| infocard.py | 요점 인포그래픽 (세로 카드 스택, 번호 원 + 헤드라인) | `from infocard import make_cards; make_cards("제목", [("1","헤드","설명","둘째줄")], "assets/x.png", sub="부제")` |
| gif_steps.py | 절차형 4단계 팝인 GIF | 스크립트 내 예시 참조. 고정 그리드 유지(겹침 금지) |
| og_card.py | 공유 카드 1200×630 (제목 조판) | `python3 scripts/og_card.py "<제목>" assets/슬러그.jpg assets/og/슬러그.jpg` |
| freebie_gen.py | 무료나눔 아이템 생성 (1:1, 단일 오브젝트, 흰 배경) | `POLLO_API_KEY=... python3 scripts/freebie_gen.py <출력폴더> "latte=a cup of latte" ...` |
| pin_gen.py | 구 Pinterest 핀 생성기 (v2는 scratchpad, §8) | — |

### 외부 의존 (hometory-note repo)

`og_card.py`는 hometory-note의 조판 유틸을 import한다:
`공용/로블록스_옷가게/디자인/엣시/수채화_K스위츠/generator/`
- `layout_qc.py` — `Canvas.image()/text()`로 배치하고 **`check(margin)` 통과해야 저장.**
  겹침 사고가 반복돼 의무화한 절차다. `OVERLAP:`이 뜨면 행간·간격을 조정하고 다시 검사.
- `transparentize.py` — 모서리 플러드필 투명화. ⚠️ **이미 투명한 PNG에 다시 돌리면 검정이 된다.**

즉 블로그 repo만 클론하면 `og_card.py`가 깨진다 → **두 repo를 나란히 클론**할 것.

### 폰트 (시스템 폰트로 대체 금지)

- 웹: 제목 고운바탕(Gowun Batang) / 본문 Noto Sans KR — `_includes/head.html`에서 로드
- PIL 조판: `/root/.fonts/SongMyung-Regular.ttf`(송명), `GreatVibes-Regular.ttf`,
  `/usr/share/fonts/truetype/nanum/NanumSquareRound{R,B}.ttf`

### Pollo API 키

hometory-note repo의 `CLAUDE.md` 시크릿 규칙대로 **Drive `secret/API_상세/POLLO API.md`**에서
확인한다. 매번 사용자에게 묻지 말 것. **키는 절대 커밋 금지** — 환경변수/scratchpad만.

---

## 4. 인터랙션 — `assets/js/anim.js` 7블록

각 블록은 독립 IIFE고, 대상 요소가 없으면 즉시 return한다. JS가 죽어도 콘텐츠는 그대로 보인다.

1. **스크롤 등장** — IntersectionObserver로 `.reveal` 팝인. 이징 `cubic-bezier(.22,.98,.36,1.02)`.
   빠른 스크롤로 관찰을 놓치는 사고가 있어 **120ms 스로틀 스윕 폴백**이 함께 돈다.
2. **Pinterest 저장 버튼** — 본문·스토리·상품 이미지 위에 얹음
3. **글 모아보기 검색 + 카테고리 필터** (`posts.md`)
4. **글 목차** — 소제목 3개 이상일 때만 생성
5. **스티키 헤더** — 스크롤 시 압축 + 글 제목 표시 (좁은 화면에선 도토리만)
6. **공유 버튼** — `navigator.share` 있으면 기기 공유창(카톡 공유 가능), 없으면 링크 복사
7. **랜딩 카운트업 + 비디오 화면 진입 시 재생**

`prefers-reduced-motion: reduce`는 전 블록에서 존중한다 — 없애지 말 것.

---

## 5. 디자인 원칙 (사용자 강력 지시 — 어기면 되돌리게 된다)

- **막대(선)로 강조하지 않는다.** 세로 막대(`border-left`)·가로 룰·밑줄 강조 **전부 금지.**
  "AI가 만든 것처럼 보인다"는 이유로 두 번 지적받았다. 위계는 **크기·굵기·색·여백**으로만.
  CSS뿐 아니라 **PIL 이미지 조판도 동일** (`d.rectangle`로 구분선 긋지 말 것).
  minima 테마 기본값에도 막대가 있어 `main.scss`에서 명시적으로 죽여놨다
  (`.site-header`/`.site-footer` border, `blockquote` border-left, `pre`/`code` border).
  이 override를 지우면 **검은 5px 헤더 막대가 부활한다** (실제 사고).
- **한글 조판**: `word-break: keep-all` 유지 — 단어 중간 줄바꿈 방지가 가독성의 핵심.
  본문 17px / 행간 1.85 / 제목 자간 -.022em.
- **팔레트**: 크림 `#FAF7F2` · 블러시 `#BA626A` · 잉크 `#3E322E` · 세이지 `#8B9E7E`
- **이미지 중심 전략**(사용자 정의): "필요한 사항을 명확히 쉽게 전달." 글마다 최소
  히어로 1장 + 인포카드/GIF 1~2장. 긴 문단보다 짧은 문단과 시각물 교차.

---

## 6. 자동화 루틴 2개 (Routines)

둘 다 이 세션(`persistent_session_id`)에 바인딩돼 있고, `list_triggers`로 확인할 수 있다.

| 트리거 ID | 이름 | cron (UTC) | KST |
|---|---|---|---|
| `trig_01GAdMLyJ1qjGrBi4eRTYEr2` | 블로그 일일 발행 | `0 22 * * *` | 매일 07:00 |
| `trig_01DPPQy7JysMeC2Ev2GxDmAS` | 무료나눔 드랍 | `30 22 */3 * *` | 3일마다 07:30 |

⚠️ cron은 **UTC**로 저장된다. KST(UTC+9) 07:00 = 전날 22:00 UTC.

**일일 발행이 발화하면** 하는 일 (상세는 `../CLAUDE.md`):
`글감백로그_AI시리즈.md` 최상단 미발행 글감 → **WebSearch로 최신 수치 확인**(모델 지식은 낡음,
확인 못한 숫자는 쓰지 않는다) → 본문 800자+·소제목 3개+ → 히어로 1장 + 인포카드 1~2장 →
OG 카드 → AI 공시 문구 → 백로그 `- [x]` 체크 → `check_build.py` → 커밋·푸시 → curl 200 확인.

**드랍이 발화하면**: `무료나눔_테마백로그.md` 최상단 테마(시즌 임박 우선)로 **4종** 생성 →
투명화 → **전수 육안 검수** → `png/`(원본 3000px) + `thumb/`(500·1000px, **크림 배경 합성** —
투명 PNG를 그냥 JPEG로 만들면 검게 된다) + ZIP(LICENSE 동봉) → `_data/freebies.yml` 맨 아래에
회차 추가(**`date` 필수** — 방문자가 주기를 보고 재방문한다) → `_config.yml`의 `next_drop`을
3일 후로 갱신 → 드랍 소개 글 1편 → 커밋·푸시.
※ Vol.1에서 보류한 `blossom`(벚꽃) PNG가 이미 있으니 봄 팩에 넣을 것.

첫 자동 발행은 2026-08-22 `ai-image-cost`로 정상 작동을 확인했다.

---

## 7. 실제로 터진 사고들 — 같은 걸 또 밟지 말 것

전부 2026-08-21~22에 실제로 일어났다. 배포 절차가 이 목록에서 나왔다.

| # | 사고 | 원인 | 규칙 |
|---|---|---|---|
| 1 | **사이트 전체가 옛 버전에 멈춤 / `/shop/` 404** | `_data/products.yml`의 `desc: "사랑해", "..."` — 큰따옴표로 시작한 값 뒤에 쉼표. YAML 한 줄이 깨지면 **Jekyll 빌드가 통째로 실패**하고 기존 페이지는 멀쩡해 보여서 발견이 늦다 | **푸시 전 `python3 scripts/check_build.py` 필수.** 한국어 설명에 따옴표가 들어가면 값 전체를 작은따옴표로: `desc: '"사랑해" ...'` |
| 2 | `CLAUDE.html`이 공개 사이트·사이트맵에 게시됨 | `exclude` 누락 | `exclude`에서 `docs/`·`CLAUDE.md`·`scripts/`·`_unpublished_en/`·`README.md`를 **절대 빼지 말 것** |
| 3 | 발행 날짜가 하루 밀려 표시 | `timezone` 미설정 → UTC 계산 | `_config.yml`의 `timezone: Asia/Seoul` 삭제 금지 |
| 4 | 폰에서 메뉴가 펼쳐진 채 배너·콘텐츠를 덮음 | 헤더 재작성 시 minima 햄버거(`nav-trigger` 체크박스 + `menu-icon`) 구조 누락 | `_includes/header.html`의 해당 구조 유지. 현재는 카드형 드롭다운(패널 `top:52px`, `min-width:210px`, `z-index:200`) |
| 5 | 소소 캐릭터 배경이 검게 나옴 | 이미 투명한 PNG에 `transparentize` 재적용 | 원본 알파를 그대로 쓰고, JPG로 만들 땐 크림 배경에 `alpha_composite` |
| 6 | 가로 7px 넘침 / 빠른 스크롤 시 빈 화면 | 스토리 슬라이드 대기 위치가 화면 밖 | `overflow-x: clip` + 모바일은 세로 등장 + 스윕 폴백 |
| 7 | 검은 5px 헤더 막대 부활 | 내 override를 지우자 minima 기본값이 노출 | `main.scss`의 명시적 `border: none` 유지 (§5) |
| 8 | Pinterest 핀이 썸네일에서 뭉개짐 | 이미 글자가 있는 상품 커버 위에 또 글자를 얹음 | 낱개 아이템을 추출해 **큰 숫자 + 헤드라인 + 격자** 구조로 (§8 `pin_v2.py`) |

### 배포 체크리스트 (매번)

```bash
cd /home/user/aijhmin1031-eng.github.io      # git 명령은 반드시 repo 루트에서
python3 scripts/check_build.py               # ❌면 절대 푸시하지 말 것
git add -A && git commit -m "..." && git push -u origin main
# 1~2분 후
curl -s -o /dev/null -w '%{http_code}\n' https://aijhmin1031-eng.github.io/post/슬러그/
curl -s https://aijhmin1031-eng.github.io/ | grep 슬러그          # 홈 노출 확인
curl -s https://aijhmin1031-eng.github.io/sitemap.xml | grep 슬러그 # 사이트맵 확인
```
200이 아니면 빌드 실패를 의심한다. 사이트맵에 **의도한 URL만** 실렸는지도 본다.

---

## 8. 브라우저 실측 검증 (Playwright)

CSS·애니메이션·모바일 레이아웃은 눈으로 못 보니 수치로 재야 한다.
스크립트는 세션 scratchpad의 `pw/`에 있었다 (`mobile_check.js`·`menu_test.js`·
`phase2_test.js`·`landing_test.js`·`design_check.js`). 다시 만들 때 필요한 두 가지:

```js
// 1) 프록시 설정 필수 — 없으면 ERR_CONNECTION_RESET
const browser = await chromium.launch({
  executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  proxy: { server: process.env.HTTPS_PROXY, bypass: 'localhost,127.0.0.1' },
});
```
```bash
# 2) 외부 사이트는 프록시에 막히므로 로컬 미러로 검사한다
cd _site_or_mirror && python3 -m http.server 8777
```
측정 항목: 가로 넘침(`scrollWidth > clientWidth`), `.reveal` 미등장 개수,
터치 영역 44px 미달, 콘솔 오류. 이 절차로 사고 #4·#6·#7을 잡았다.

### 마케팅 도구 (scratchpad, repo 미포함 — 필요하면 재작성)

- `pins/pin_v2.py` — 현행 핀 생성기 (큰 숫자 + 헤드라인 + 아이템 격자)
- `items/extract.py` — 상품 미리보기에서 낱개 오브젝트 추출 (scipy connected components)
- `blog/blog_brand_compose.py` — 배너·프로필·파비콘 조립 (막대 제거판)
- 홍보 mp4 웹 최적화: `ffmpeg -vf scale=720:-2 -crf 28 -preset slow -an -movflags +faststart`

---

## 9. Drive · 외부 계정

| 자원 | ID / 주소 |
|---|---|
| `SOSO_작업실_블로그` (블로그 폴더) | `1eEzHRf4dsqcuxlVM5qkWbgEdmFWH8GpX` |
| ├ 블로그_운영계획.md | `188J6Vq2pSPoWG9ybOgN3BA9fzPpYjioD` |
| └ 핀터레스트_핀 | `1evYAiFmEErpm1k7uCUjZ5eyzmeetSLH-` |
| 　├ 01_무료나눔_핀(먼저올리기) | `1dzgPHVa67FIcfdVOA_akJok-OWzvl549` |
| 　└ 02_상품_핀 | `1O55G_HKRTmecfIVj3otJuv1--TdrLTJt` |
| Search Console 토큰 | `.secrets/gws-cli/gsc_searchconsole_token.json` — `1XqLJbJjgHlQ1qZh9yGqdJZV3HRrYh7L_` |
| Drive 업로드 토큰 | `.secrets/gws-cli/gws_mobile_token.json` — `1p9qhuro1Cw3LwhSjkYZhKNhDDhCSsmxE` |

- **Google Search Console**: `aijhmin1031-eng.github.io` 속성 등록 완료, 사이트맵 제출됨.
  소유확인은 `_config.yml`의 `webmaster_verifications.google` + `google*.html` 파일 둘 다 유지.
  API scope는 `webmasters` + `siteverification`. 색인 조회는
  `searchconsole.googleapis.com/v1/urlInspection/index:inspect`.
- **네이버 서치어드바이저**: 소유확인 완료(`naver*.html`). 사이트맵 제출은 미완.
- **Payhip 상점**: https://payhip.com/SosotoryStudio (⚠️ 철자 Sos**o**tory — o다)
- **Pinterest**: 계정 생성됨. API는 Trial=샌드박스 전용이라 자동화 불가 → **수동 업로드가 빠르다**.

토큰은 `download_file_content`로 받아 **scratchpad에만** 두고, repo에 커밋하지 않는다.
Drive 업로드는 `drive_up.py`를 토큰과 **같은 디렉토리**에 두고 실행.

---

## 10. 현재 진행 상황

**완료**
- 글 5편 발행 (2026-08-21 4편 + 08-22 1편 자동 발행)
- 브랜드 일습(배너·프로필·파비콘 4종·마스코트), 랜딩 페이지 `/start/`
- 한국어 상품 페이지 `/shop/` (9종 + FAQ), 무료나눔 `/freebies/` (Vol.1 4종, 라이트박스)
- 홈 스토리 구성 + "처음 오셨다면" + 스티키 헤더 + 검색·필터 + 목차 + 공유 버튼
- 구글·네이버 소유확인, 사이트맵 제출(구글), OG 카드, FAQ 구조화 데이터
- 자동화 루틴 2개 (일일 발행 1회 정상 작동 확인)

**대기 중 / 다음에 할 일** (우선순위 순)
1. **`_data/products.yml`의 `url` 9개가 전부 상점 첫 페이지**(`payhip.com/SosotoryStudio`)다.
   상품별 개별 링크로 교체해야 한다 — Payhip 등록 완료분의 상품 URL을 사용자에게 받아 반영.
2. **애드센스 신청**: 글 15편 목표(현재 5편). 필수 페이지는 완비.
   승인 후 `_config.yml`의 `google_adsense` 주석 해제.
3. Payhip 번들 2종 등록 (사용자 작업) — 컴플리트 $16.99(kcc), 캘리 트릴로지 $9.99(kct)
4. Pinterest 보드 5개 생성 + 무료나눔 핀 먼저 업로드 (사용자 작업)
5. 캘리(kp·kph·hg)·비즈니스(kbp) v2 핀 미제작 — 미리보기 구조가 달라 낱개 추출 실패
6. 네이버 사이트맵 제출 / 구글 색인 대기 (크롤링은 됐고 색인 전)
7. Payoneer 심사 답변 대기 → 승인되면 Etsy 오픈 (hometory-note repo 쪽 작업)

---

## 11. 절대 규칙 (hometory-note CLAUDE.md 승계)

- **API 키·토큰·client_secret을 repo에 커밋 금지** — 문서·코드·커밋 메시지 전부.
  Drive secret 폴더 + 세션 scratchpad/환경변수만.
- **모델 ID를 커밋·PR·코드 주석에 넣지 말 것.**
- 개인정보(본명·주소·계정번호)·가족 사진 커밋 금지.
- IP 단어(캐릭터명·브랜드명) 사용 금지. 글 말미 **AI 공시 문구 고정**:
  `_이 블로그의 글은 직접 겪은 경험을 바탕으로 작성하며, 일부 이미지 제작에 AI 도구를 활용합니다._`
- 특정 플랫폼 비방 금지. README에 특정 플랫폼명 고정 금지(멀티채널 판매).
- `docs/`·`_unpublished_en/`·`google*.html`·`naver*.html` 삭제 금지.
- git 명령은 **반드시 repo 루트에서** (cd 잔류로 엉뚱한 repo에 커밋한 사고 다수).
- 작업 단위마다 커밋·푸시하고, 관련 문서(CLAUDE.md·백로그·이 문서)를 함께 갱신한다.

---

## 12. 관련 repo

| repo | 역할 |
|---|---|
| `aijhmin1031-eng/hometory-note` | 본체. 상품 제작 공정·Drive 폴더맵·시크릿 규칙·엣시/Payhip 등록팩. 인수인계는 `공용/로블록스_옷가게/기획/HANDOFF_신규디자인세션.md` |
| `aijhmin1031-eng/aijhmin1031-eng.github.io` | 이 블로그 |
| `aijhmin1031-eng/sinatv-studio` | 유튜브(시나TV) 전용 — 이 블로그와 무관, 건드리지 말 것 |
