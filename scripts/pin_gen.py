#!/usr/bin/env python3
"""Pinterest 핀 생성 — 1000x1500 세로, 커버 + 헤드라인 밴드 (겹침 검사 포함)."""
import os, sys
sys.path.insert(0, '/home/user/hometory-note/공용/로블록스_옷가게/디자인/엣시/수채화_K스위츠/generator')
from layout_qc import Canvas
from PIL import Image, ImageDraw, ImageFont

PKG = '/home/user/hometory-note/공용/로블록스_옷가게/디자인/엣시/판매패키지'
OUT = os.path.dirname(os.path.abspath(__file__)) + '/out'
os.makedirs(OUT, exist_ok=True)

CREAM, INK, BLUSH, SAGE = (250,247,242), (62,50,46), (186,98,106), (139,158,126)
PLAY = '/root/.fonts/PlayfairDisplay[wght].ttf'
VIBES = '/root/.fonts/GreatVibes-Regular.ttf'

def pf(size, weight=700):
    f = ImageFont.truetype(PLAY, size)
    try: f.set_variation_by_axes([weight])
    except Exception: pass
    return f

W, H = 1000, 1500
IMG_H = 1000         # 상단 이미지 영역
BAND_Y = IMG_H       # 텍스트 밴드 시작

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def make_pin(cover, headline, sub, meta, out_name):
    c = Canvas(W, H, CREAM)
    d = ImageDraw.Draw(c.img)

    # 상단 커버 (정사각 → 상단 크롭해 인물/오브젝트 위주 노출)
    im = Image.open(f'{PKG}/{cover}').convert('RGB')
    s = W / im.width
    im = im.resize((W, int(im.height * s)), Image.LANCZOS)
    im = im.crop((0, 0, W, IMG_H))
    c.img.paste(im, (0, 0))

    # 이미지 아래 구분선
    d.rectangle([0, IMG_H-4, W, IMG_H], fill=BLUSH)

    # 텍스트 블록을 밴드 중앙에 배치
    f_h = pf(58, 800); f_s = pf(30, 500); f_m = pf(30, 700)
    hl = wrap(d, headline, f_h, W - 120)
    sl = wrap(d, sub, f_s, W - 160)
    block_h = len(hl)*92 + 8 + len(sl)*54 + 18 + 54
    band_top, band_bot = IMG_H, H - 96
    y = band_top + max(24, (band_bot - band_top - block_h) // 2)

    for i, ln in enumerate(hl):
        c.text(W//2, y, ln, f_h, INK, anchor='center', tag=f'h{i}')
        y += 92
    y += 8
    for i, ln in enumerate(sl):
        c.text(W//2, y, ln, f_s, (111,99,91), anchor='center', tag=f's{i}')
        y += 54
    y += 18
    tw = d.textlength(meta, font=f_m)
    d.rounded_rectangle([W//2 - tw//2 - 26, y - 8, W//2 + tw//2 + 26, y + 46], radius=26, fill=BLUSH)
    c.text(W//2, y, meta, f_m, (255,255,255), anchor='center', tag='meta')

    # 서명
    f_v = ImageFont.truetype(VIBES, 40)
    c.text(W//2, H - 74, "SOSO's Atelier", f_v, BLUSH, anchor='center', tag='sig')

    bad = c.check(margin=10)
    if bad: raise SystemExit(f'OVERLAP {out_name}: {bad}')
    c.img.save(f'{OUT}/{out_name}', quality=90)
    print('OK', out_name)

PINS = [
 # (cover, headline, sub, meta, filename)
 ('ksc_P1_cover.png', 'Korean Cafe Clipart Collection',
  'Hanbok, bingsu, teapots and cherry blossoms — hand-painted watercolor PNGs', '62 PNG · 3000px', 'pin_ksc_1.jpg'),
 ('ksc_P1_cover.png', '62 Watercolor Cliparts for Your Craft Projects',
  'Transparent backgrounds. Drop straight into Canva or Procreate.', 'COMMERCIAL USE', 'pin_ksc_2.jpg'),
 ('kfr_P1_cover.png', 'Watercolor Frames & Menu Cards',
  'Empty centers ready for your own text — perfect for menus and invites', '12 PNG · 3000px', 'pin_kfr_1.jpg'),
 ('kfr_P1_cover.png', 'Pretty Frames for Menus and Invitations',
  'Add your text in Canva or Word. No design skills needed.', '12 DESIGNS', 'pin_kfr_2.jpg'),
 ('kmk_P1_cover.png', 'Korean Food Menu Templates',
  '4 editable menu layouts plus 10 hand-painted dish illustrations', 'MENU KIT', 'pin_kmk_1.jpg'),
 ('kmk_P1_cover.png', 'Design a Cafe Menu in Minutes',
  'Watercolor menu templates for small restaurants and cafes', 'A4 TEMPLATES', 'pin_kmk_2.jpg'),
 ('kbp_P1_cover.png', 'Small Business Template Kit',
  'Price lists, vouchers, business cards — all in soft watercolor style', '9 TEMPLATES', 'pin_kbp_1.jpg'),
 ('kbp_P1_cover.png', 'Price List Templates for Small Shops',
  'Nail salons, florists, photographers — edit and print today', 'BUSINESS KIT', 'pin_kbp_2.jpg'),
 ('kp_P1_cover.png', 'Korean Calligraphy Brush Designs',
  '12 hand-brushed Hangul words in SVG, PNG and EPS', '12 DESIGNS · SVG', 'pin_kp_1.jpg'),
 ('kph_P1_cover.png', 'Korean Phrases in Brush Lettering',
  '"I love you", "You did well today" — meanings verified by a native speaker', '9 PHRASES', 'pin_kph_1.jpg'),
 ('hg_P1_cover.png', 'Hangul Calligraphy Starter Set',
  '15 Korean words with gold, white ink and hanji bonus versions', '15 WORDS + BONUS', 'pin_hg_1.jpg'),
 ('kcc_P1_cover.png', 'The Complete Korean Watercolor Collection',
  'Every clipart, frame, menu and business template in one bundle', '110+ FILES', 'pin_kcc_1.jpg'),
 ('kcc_P1_cover.png', 'Save 40% with the Complete Bundle',
  'Clipart, frames, menu kit and business pages together', 'BEST VALUE', 'pin_kcc_2.jpg'),
 ('kct_P1_cover.png', 'Hangul Calligraphy Trilogy',
  'All three brush lettering collections — 36 designs, tattoo-safe', '36 DESIGNS', 'pin_kct_1.jpg'),
]

if __name__ == '__main__':
    for p in PINS: make_pin(*p)
    print('총', len(PINS), '장')
