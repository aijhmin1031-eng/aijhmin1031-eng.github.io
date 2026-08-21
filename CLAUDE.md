# CLAUDE.md — 소소 부업 연구소 블로그 발행 공정

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

## 브랜드

- 마스코트 소소(다람쥐 화가, 핑크 베레모) — hometory-note repo의 소소 캐릭터와 동일
- 팔레트: 크림 #FAF7F2 · 블러시 #BA626A · 잉크 #3E322E · 세이지 #8B9E7E
- 폰트: 제목 고운바탕 / 본문 Noto Sans KR (웹) · PIL 조판은 송명+NanumSquareRound
- 수채화 STYLE 접미사는 `scripts/hero_gen.py` 안에 고정 — 임의 변경 금지

## 금지

- 개인정보(본명·주소·계정번호)·API 키·토큰 커밋 금지
- `_unpublished_en/`(영어판 보관), `docs/`는 빌드 제외 — 지우지 말 것
- 네이버/구글 확인 파일(naver*.html, google*.html) 삭제 금지
