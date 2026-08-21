#!/usr/bin/env python3
"""무료나눔 팩 생성기 — 테마별 수채화 5종 (단일 오브젝트, 투명화 전 원본).

사용: POLLO_API_KEY=... python3 freebie_gen.py <출력폴더> "이름=영문설명" ...
예:  python3 freebie_gen.py /tmp/pack "maple=a single red maple leaf" "chestnut=..."
STYLE 접미사는 브랜드 고정 — 임의 변경 금지. 생성 후 반드시 투명화+육안검수.
"""
import json, os, sys, time, urllib.request

BASE = "https://pollo.ai/api/platform"
STYLE = ("delicate hand-painted watercolor illustration, soft gouache texture with "
         "gentle color washes, charming preppy storybook style, pastel palette of "
         "blush pink, cream, soft blue and warm yellow, fine thin linework accents, "
         "single object centered with generous margin, isolated on plain white "
         "background, no text, no letters, no watermark")

def req(method, url, body=None, key=None):
    r = urllib.request.Request(url, method=method,
        headers={"x-api-key": key, "content-type": "application/json"},
        data=json.dumps(body).encode() if body else None)
    with urllib.request.urlopen(r, timeout=60) as resp:
        return json.loads(resp.read())

def gen(subject, out_png, key):
    body = {"input": {"prompt": f"{subject}, {STYLE}", "aspectRatio": "1:1",
                      "resolution": "1K", "quality": "medium"}}
    out = req("POST", f"{BASE}/generation/openai/gpt-image-2-0/image", body, key)
    task = out["data"]["taskId"]
    deadline = time.time() + 420
    while time.time() < deadline:
        time.sleep(5)
        st = req("GET", f"{BASE}/generation/{task}/status", key=key)
        g = st["data"]["generations"]
        if g and g[0]["status"] == "succeed":
            urllib.request.urlretrieve(g[0]["url"], out_png); return True
        if g and g[0]["status"] == "failed":
            print("failMsg:", g[0].get("failMsg")); return False
    return False

if __name__ == "__main__":
    key = os.environ["POLLO_API_KEY"]
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)
    for spec in sys.argv[2:]:
        name, subject = spec.split("=", 1)
        print("OK" if gen(subject, f"{outdir}/{name}.png", key) else "FAIL", name, flush=True)
