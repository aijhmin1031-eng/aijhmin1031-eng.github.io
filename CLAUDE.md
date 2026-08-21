# CLAUDE.md — 소소의 작업실 블로그 발행 공정

이 repo는 GitHub Pages(Jekyll/minima) 블로그다. **main에 푸시하면 1~2분 내 자동 배포**된다.
사이트: https://aijhmin1031-eng.github.io/

## 일일 발행 공정 (매일 1편)

0. **이미지 중심 원칙 (전략)** — 방문자가 스크롤만 해도 이해되게. 글마다 최소:
   히어로 1장 + 정보 인포그래픽 1~2장(핵심 요점은 `scripts/infocard.py` 카드,
   절차는 `scripts/gif_steps.py` GIF). 긴 문단보다 짧은 문단+시각물 교차.
   **최신 트렌드**: 작성 전 WebSearch로 해당 주제의 최근 동향·수치를 확인해 반영한다
   (모델 지식은 낡았을 수 있음). 확인 못한 수치는 쓰지 않는다.
1. `docs/글감백로그_AI시리즈.md`에서 **최상단 미발행(- [ ]) 글감**을 고른다.
2. `_posts/YYYY-MM-DD-슬러그.md` 작성. front matter:
   `layout: post / title / date(발행 시각은 현재보다 과거로! 미래면 빌드 제외됨) / lang: ko / categories: AI부업`
3. **품질 규칙 (절대)**
   - 직접 해본 경험·구체 숫자 중심, 과장·수익 보장 표현 금지 ("월 천만" 류 금지)
   - 본문 한국어 800자 이상, 소제목(##) 3개 이상, 표나 목록으로 요점 정리
   - 말미 AI 공시 문구 고정: `_이 블로그의 글은 직접 겪은 경험을 바탕으로 작성하며, 일부 이미지 제작에 AI 도구를 활용합니다._`
   - 특정 플랫폼 비방 금지, IP(캐릭터·브랜드) 언급 금지
4. **히어로 삽화 1장**: `scripts/hero_gen.py "<영문 장면 설명>" assets/<슬러그>.jpg`
   - POLLO_API_KEY는 hometory-note repo CLAUDE.md의 시크릿 규칙대로 Drive에서 확인 (`POLLO API.md`)
   - 키는 절대 커밋 금지, scratchpad/env로만
5. 절차·단계형 내용이면 `scripts/gif_steps.py` 참고해 4단계 팝인 GIF 추가 (겹침 없는 고정 그리드 유지)
6. 발행한 글감은 백로그에서 `- [x]`로 체크 + 발행일 기입.
7. 커밋·푸시 후 `curl -s https://aijhmin1031-eng.github.io/ | grep <슬러그>`로 반영 확인.

## 무료나눔 드랍 공정 (3일 간격, **회차당 4종**)

1. `docs/무료나눔_테마백로그.md` 최상단 미발행 테마 선택 (시즌 임박 테마는 당김).
   ※ Vol.1에서 보류한 `blossom`(벚꽃)은 봄 팩에 넣을 것 — PNG는 이미 생성돼 있음.
2. `scripts/freebie_gen.py`로 **4종** 생성 → transparentize(모서리 플러드필, 내부 흰색 보존,
   3000px) → **전수 육안 검수** (이상 소품·문화 고증·스타일 이탈 시 재생성).
3. 배포 3종 세트를 `assets/freebies/`에 추가:
   - `png/soso_<이름>.png` — 원본 투명 PNG 3000px (**낱장 직접 다운로드가 기본**)
   - `thumb/soso_<이름>.jpg` 500px + `_lg.jpg` 1000px — **크림(#FAF7F2) 배경에 합성**
     (투명 PNG를 JPEG로 만들면 검게 되므로 반드시 배경 합성)
   - ZIP(LICENSE.txt 동봉 — 개인·소상공인 허용, 재판매·재배포 금지, AI 공시) — 선택지로 유지
4. **`_data/freebies.yml` 맨 아래에 새 회차 추가** (freebies.md는 이 데이터로 자동 렌더링 —
   페이지 HTML은 건드리지 말 것):
   ```yaml
   - vol: 2
     title: 홈카페 티타임
     date: 2026-08-24        # 공개일자 필수 — 방문자가 주기를 보고 재방문함
     note: 한 줄 소개
     zip: /assets/freebies/soso_teatime_vol2.zip
     items:
       - { file: teapot, label: 티팟 }   # file은 png/thumb 파일명과 일치, 4개
   ```
   그리고 `_config.yml`의 `next_drop`을 **다음 드랍일(3일 후)**로 갱신한다.
   파일명은 팩마다 유일해야 함(라이트박스 id 충돌 방지).
5. 드랍 소개 글 1편 발행 (미리보기 이미지 + 아이템 소개 + 다운로드 링크 + 상점 유도)
   — 그날의 일일 글과 별개, 짧아도 됨. categories: 무료나눔
6. 백로그 체크 + 드랍 이력 기입, 커밋·푸시, 사이트 반영 확인.
7. ZIP 누적으로 repo가 300MB를 넘기 시작하면 오래된 팩은 Drive로 이관 검토 (링크 교체).


## 사이트 위생 규칙 (반드시 지킬 것)

- `_config.yml`의 `exclude`에서 `CLAUDE.md`·`docs/`·`scripts/`·`_unpublished_en/`를 **절대 빼지 말 것**
  (내부 문서가 공개 사이트에 노출되고 사이트맵에 실림 — 2026-08-21 실제 사고).
- 글 URL은 `permalink: /post/:title/` — 한글 카테고리가 URL에 들어가지 않게 유지.
- 새 페이지/글 배포 후에는 `curl`로 사이트맵을 확인해 **의도한 URL만** 실려 있는지 점검한다.

## 브랜드

- 마스코트 소소(다람쥐 화가, 핑크 베레모) — hometory-note repo의 소소 캐릭터와 동일
- 팔레트: 크림 #FAF7F2 · 블러시 #BA626A · 잉크 #3E322E · 세이지 #8B9E7E
- 폰트: 제목 고운바탕 / 본문 Noto Sans KR (웹) · PIL 조판은 송명+NanumSquareRound
- 수채화 STYLE 접미사는 `scripts/hero_gen.py` 안에 고정 — 임의 변경 금지

## 금지

- 개인정보(본명·주소·계정번호)·API 키·토큰 커밋 금지
- `_unpublished_en/`(영어판 보관), `docs/`는 빌드 제외 — 지우지 말 것
- 네이버/구글 확인 파일(naver*.html, google*.html) 삭제 금지
