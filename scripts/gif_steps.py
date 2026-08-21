#!/usr/bin/env python3
"""블로그 인포그래픽 GIF — 단계 카드가 순차 팝인 (브랜드 팔레트, 겹침없는 고정 그리드)."""
import math, os
from PIL import Image, ImageDraw, ImageFont

W, H = 800, 450
CREAM, INK, BLUSH, SAGE = (250,247,242), (62,50,46), (186,98,106), (139,158,126)
CARD = (255,255,255)
FDIR = "/root/.fonts"
KR_B = f"{FDIR}/../../usr/share/fonts/truetype/nanum/NanumSquareRoundB.ttf"
KR_B = "/usr/share/fonts/truetype/nanum/NanumSquareRoundB.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def ease_pop(t):  # 0..1 → overshoot scale
    if t >= 1: return 1.0
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (t-1)**3 + c1 * (t-1)**2

def draw_frame(title, steps, appear, title_a):
    """appear: 각 카드의 스케일(0~1.x), title_a: 타이틀 알파 0~1"""
    im = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(im)
    ft = font(KR_B, 30)
    fs = font(KR_B, 19)
    fn = font(KR_B, 26)
    # 타이틀 (페이드 = 색 보간)
    tc = tuple(int(CREAM[i] + (INK[i]-CREAM[i]) * title_a) for i in range(3))
    tw = d.textlength(title, font=ft)
    d.text(((W-tw)//2, 42), title, font=ft, fill=tc)
    d.rectangle([W//2-40, 92, W//2+40, 95], fill=tuple(int(CREAM[i]+(BLUSH[i]-CREAM[i])*title_a) for i in range(3)))
    # 카드 4장: 고정 그리드 (x centers), 카드 160x210
    cw, ch, cy = 168, 220, 260
    xs = [110, 303, 496, 689]
    for i, (num, l1, l2) in enumerate(steps):
        s = appear[i]
        if s <= 0.02: continue
        w2, h2 = int(cw*s/2), int(ch*s/2)
        cx = xs[i]
        box = [cx-w2, cy-h2, cx+w2, cy+h2]
        d.rounded_rectangle(box, radius=int(16*s), fill=CARD, outline=(228,220,210), width=2)
        if s > 0.6:
            r = int(26*s)
            by = cy - h2 + int(52*s)
            d.ellipse([cx-r, by-r, cx+r, by+r], fill=BLUSH if i%2==0 else SAGE)
            d.text((cx, by-2), num, font=fn, fill=(255,255,255), anchor="mm")
            d.text((cx, cy+14), l1, font=fs, fill=INK, anchor="mm")
            d.text((cx, cy+44), l2, font=fs, fill=INK, anchor="mm")
        # 화살표 (다음 카드가 나타나기 시작하면)
        if i < 3 and appear[i+1] > 0.3:
            ax = (xs[i]+xs[i+1])//2
            d.line([ax-14, cy, ax+10, cy], fill=BLUSH, width=4)
            d.polygon([(ax+10, cy-7), (ax+22, cy), (ax+10, cy+7)], fill=BLUSH)
    return im

def build(title, steps, out, fps=12):
    frames = []
    t_title, t_step, dur_step = 0.25, 0.38, 0.34
    total = t_title + 4*t_step + dur_step + 1.6
    n = int(total*fps)
    for f in range(n):
        t = f / fps
        ta = min(1.0, t / t_title)
        ap = []
        for i in range(4):
            st = t_title + i*t_step
            ap.append(0.0 if t < st else ease_pop(min(1.0, (t-st)/dur_step)))
        frames.append(draw_frame(title, steps, ap, ta))
    frames[0].save(out, save_all=True, append_images=frames[1:],
                   duration=int(1000/fps), loop=0, optimize=True)
    print("saved", out, os.path.getsize(out)//1024, "KB")

KO1 = ("디지털 파일 부업, 시작 순서", [("1","정산계정","먼저 신청"),("2","상품 라인","완성하기"),("3","무심사 상점","먼저 오픈"),("4","장터 입점","(Etsy 등)")])
KO2 = ("Payhip 상점 개설 4단계", [("1","가입 · URL","철자 확인!"),("2","PayPal","연결"),("3","상품 등록","파일+설명"),("4","상점 꾸미기","About·로고")])
EN1 = ("Digital File Side Hustle: The Order", [("1","Payout","accounts first"),("2","Finish a","product line"),("3","Open a","storefront"),("4","Enter the","marketplace")])
EN2 = ("Payhip Setup in 4 Steps", [("1","Sign up","check the URL"),("2","Connect","PayPal"),("3","Add","products"),("4","Style the","store")])

if __name__ == "__main__":
    outdir = os.path.dirname(os.path.abspath(__file__)) + "/art"
    os.makedirs(outdir, exist_ok=True)
    build(*KO1, out=f"{outdir}/steps_start_ko.gif")
    build(*KO2, out=f"{outdir}/steps_payhip_ko.gif")
    build(*EN1, out=f"{outdir}/steps_start_en.gif")
    build(*EN2, out=f"{outdir}/steps_payhip_en.gif")
