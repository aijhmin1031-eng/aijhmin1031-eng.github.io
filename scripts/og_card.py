#!/usr/bin/env python3
"""공유용 OG 카드 생성 (1200x630) — 카톡·페북·X에서 링크 공유 시 보이는 이미지.

사용: python3 scripts/og_card.py "<글 제목>" <히어로이미지경로> assets/og/<슬러그>.jpg
제목이 카드에 크게 박히므로 공유 링크의 클릭률이 크게 오른다.
"""
import os, sys
sys.path.insert(0, '/home/user/hometory-note/공용/로블록스_옷가게/디자인/엣시/수채화_K스위츠/generator')
from layout_qc import Canvas
from PIL import Image, ImageDraw, ImageFont, ImageFilter

CREAM, INK, BLUSH = (250, 247, 242), (62, 50, 46), (186, 98, 106)
SONG = '/root/.fonts/SongMyung-Regular.ttf'
VIBES = '/root/.fonts/GreatVibes-Regular.ttf'
KR_R = '/usr/share/fonts/truetype/nanum/NanumSquareRoundR.ttf'
ACORN = 'assets/brand/shop_acorn.png'
W, H = 1200, 630


def wrap(d, text, font, maxw):
    """한국어는 공백 기준 + 글자 단위 보조 줄바꿈."""
    out, cur = [], ''
    for token in text.split():
        t = (cur + ' ' + token).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                out.append(cur)
            cur = token
            while d.textlength(cur, font=font) > maxw:
                cut = len(cur)
                while cut > 1 and d.textlength(cur[:cut], font=font) > maxw:
                    cut -= 1
                out.append(cur[:cut])
                cur = cur[cut:]
    if cur:
        out.append(cur)
    return out


def make(title, hero, out_path):
    c = Canvas(W, H, CREAM)
    d = ImageDraw.Draw(c.img)

    # 오른쪽에 히어로 이미지를 흐릿하게 깔고 크림으로 페이드
    if hero and os.path.exists(hero):
        im = Image.open(hero).convert('RGB')
        s = max(W / im.width, H / im.height)
        im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
        left = max(0, (im.width - W) // 2)
        im = im.crop((left, 0, left + W, H))
        im = im.filter(ImageFilter.GaussianBlur(1.2))
        c.img.paste(im, (0, 0))
        veil = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        vd = ImageDraw.Draw(veil)
        for x in range(W):
            a = int(252 * min(1.0, max(0.0, (W * 0.74 - x) / (W * 0.52))))
            vd.line([(x, 0), (x, H)], fill=CREAM + (a,))
        c.img.paste(Image.alpha_composite(c.img.convert('RGBA'), veil).convert('RGB'), (0, 0))

    # 좌측 텍스트 영역
    d.rectangle([0, 0, 12, H], fill=BLUSH)
    f_t = ImageFont.truetype(SONG, 62)
    f_s = ImageFont.truetype(KR_R, 27)
    f_v = ImageFont.truetype(VIBES, 38)

    lines = wrap(d, title, f_t, 690)[:3]
    y = (H - (len(lines) * 84 + 120)) // 2
    for i, ln in enumerate(lines):
        c.text(64, y, ln, f_t, INK, tag=f'l{i}')
        y += 84
    d.rectangle([64, y + 14, 190, y + 19], fill=BLUSH)
    c.text(64, y + 44, '소소의 작업실 · 만들고, 팔고, 그 과정을 기록합니다', f_s, (111, 99, 91), tag='sub')

    if os.path.exists(ACORN):
        c.image(ACORN, W - 118, H - 132, 104, tag='acorn')
    c.text(W - 118, H - 62, "SOSO's Atelier", f_v, BLUSH, anchor='center', tag='sig')

    bad = c.check(margin=8)
    if bad:
        raise SystemExit(f'OVERLAP {out_path}: {bad}')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    c.img.save(out_path, quality=88, optimize=True)
    print('OK', out_path, os.path.getsize(out_path) // 1024, 'KB')


if __name__ == '__main__':
    make(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else '', sys.argv[3])
