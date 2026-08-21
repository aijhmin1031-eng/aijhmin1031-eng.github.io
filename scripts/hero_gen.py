#!/usr/bin/env python3
"""블로그 히어로 삽화 생성 (Pollo GPT Image 2, 수채화 3:2, 웹용 1200px JPEG).

사용: POLLO_API_KEY=... python3 hero_gen.py "<영문 장면 설명>" assets/slug.jpg
STYLE 접미사는 브랜드 고정 — 임의 변경 금지.
"""
import io, json, os, sys, time, urllib.request

BASE = "https://pollo.ai/api/platform"
STYLE = ("delicate hand-painted watercolor illustration, soft gouache texture with "
         "gentle color washes, charming preppy storybook style, pastel palette of "
         "blush pink, cream, soft blue and warm yellow, fine thin linework accents, "
         "cozy inviting mood, no text, no letters, no watermark")

def req(method, url, body=None, key=None):
    r = urllib.request.Request(url, method=method,
        headers={"x-api-key": key, "content-type": "application/json"},
        data=json.dumps(body).encode() if body else None)
    with urllib.request.urlopen(r, timeout=60) as resp:
        return json.loads(resp.read())

def gen(subject, out_path, key, timeout_s=420):
    body = {"input": {"prompt": f"{subject}, {STYLE}", "aspectRatio": "3:2",
                      "resolution": "1K", "quality": "medium"}}
    out = req("POST", f"{BASE}/generation/openai/gpt-image-2-0/image", body, key)
    task = out["data"]["taskId"]
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        time.sleep(5)
        st = req("GET", f"{BASE}/generation/{task}/status", key=key)
        g = st["data"]["generations"]
        if g and g[0]["status"] == "succeed":
            tmp = out_path + ".tmp.png"
            urllib.request.urlretrieve(g[0]["url"], tmp)
            from PIL import Image
            im = Image.open(tmp).convert("RGB")
            im.thumbnail((1200, 1200), Image.LANCZOS)
            im.save(out_path, quality=85, optimize=True)
            os.remove(tmp)
            return True
        if g and g[0]["status"] == "failed":
            print("failMsg:", g[0].get("failMsg")); return False
    return False

if __name__ == "__main__":
    subject, out_path = sys.argv[1], sys.argv[2]
    key = os.environ["POLLO_API_KEY"]
    ok = gen(subject, out_path, key)
    print("OK" if ok else "FAIL", out_path)
    sys.exit(0 if ok else 1)
