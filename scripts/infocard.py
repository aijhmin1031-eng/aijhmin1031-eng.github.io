#!/usr/bin/env python3
"""브랜드 정보카드 인포그래픽 — 세로 카드 스택 PNG (겹침 없는 고정 그리드).

사용 예:
  from infocard import make_cards
  make_cards("제목", [("1","헤드라인","설명 한 줄","설명 두 줄"), ...], "assets/x.png")
카드 수 제한 없음(3~5 권장). 색은 블러시/세이지 교차.
"""
from PIL import Image, ImageDraw, ImageFont

CREAM, INK, BLUSH, SAGE = (250,247,242), (62,50,46), (186,98,106), (139,158,126)
CARD, LINE, SUB = (255,255,255), (228,220,210), (111,99,91)
SONG = "/root/.fonts/SongMyung-Regular.ttf"
KR_B = "/usr/share/fonts/truetype/nanum/NanumSquareRoundB.ttf"
KR_R = "/usr/share/fonts/truetype/nanum/NanumSquareRoundR.ttf"

def make_cards(title, items, out, w=1100, sub=None):
    ch, gap, top = 190, 26, 150
    if sub: top += 46
    h = top + len(items)*(ch+gap) + 40
    im = Image.new("RGB", (w, h), CREAM)
    d = ImageDraw.Draw(im)
    f_t = ImageFont.truetype(SONG, 52)
    f_sub = ImageFont.truetype(KR_R, 26)
    f_h = ImageFont.truetype(KR_B, 34)
    f_b = ImageFont.truetype(KR_R, 25)
    f_n = ImageFont.truetype(KR_B, 40)
    tw = d.textlength(title, font=f_t)
    d.text(((w-tw)//2, 44), title, font=f_t, fill=INK)
    d.rectangle([(w-120)//2, 116, (w+120)//2, 120], fill=BLUSH)
    if sub:
        sw = d.textlength(sub, font=f_sub)
        d.text(((w-sw)//2, 138), sub, font=f_sub, fill=SUB)
    y = top
    for i, it in enumerate(items):
        num, head, l1 = it[0], it[1], it[2]
        l2 = it[3] if len(it) > 3 else ""
        col = BLUSH if i % 2 == 0 else SAGE
        d.rounded_rectangle([40, y, w-40, y+ch], radius=18, fill=CARD, outline=LINE, width=2)
        d.rounded_rectangle([40, y, 52, y+ch], radius=6, fill=col)
        cx, cy = 118, y + ch//2
        d.ellipse([cx-34, cy-34, cx+34, cy+34], fill=col)
        d.text((cx, cy-3), num, font=f_n, fill=(255,255,255), anchor="mm")
        d.text((186, y+34), head, font=f_h, fill=INK)
        d.text((186, y+88), l1, font=f_b, fill=SUB)
        if l2:
            d.text((186, y+126), l2, font=f_b, fill=SUB)
        y += ch + gap
    im.save(out, optimize=True)
    print("saved", out, im.size)

if __name__ == "__main__":
    make_cards("샘플 카드", [("1","헤드라인","설명","둘째 줄")], "sample.png")
