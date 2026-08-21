---
layout: post
title: "Making Sellable Clipart with AI: What Separates a Product from a Hobby"
date: 2026-08-21 08:30:00 +0900
lang: en
categories: english production
---

Making clipart with AI image generators is a well-known side hustle by now.
The problem: **raw AI output is not a product.** After actually producing a
watercolor clipart set of dozens of images and taking it to market-ready,
here is what separates a hobby folder from something people pay for.

![Watercolor illustration of a painting workspace with palette, brushes and swatches]({{ "/assets/hero_atelier.jpg" | relative_url }})

## 1. Lock the style with a fixed prompt suffix

Clipart sells as a **set**. Buyers download 30–60 images and mix them in
their own designs — if the art style drifts between images, the set is
worthless. The fix is simple: append the **same style sentence to every
prompt** and never touch it:

> "...delicate hand-painted watercolor illustration, soft pastel palette,
> isolated on plain white background, no text"

Change only the subject (strawberry cake, flowers, teacup...). Do this and a
set produced over weeks still looks painted by one hand.

## 2. Background removal is half the work

People buy clipart to **layer it over their own designs**, so transparent
PNGs are the standard. But if you naively delete "all white pixels" from an
AI image generated on a white background, you punch holes through the white
*inside* the artwork — powdered sugar, highlights, white petals.

What worked for me is removing only the white that is **connected to the
image corners** (flood fill from the edges), which preserves interior
whites, plus a slightly softened edge so nothing looks jagged at scale.
Whatever tool you use, verify one thing: does interior white survive?

## 3. Inspect every single image before selling

AI produces a steady percentage of wrong results. Real rejects from my set:

- Asked for a Korean rice cake, got a Western layer cake (cultural accuracy)
- Unrequested props appearing in the background
- A traditional Korean table rendered as Victorian furniture

Review the whole set image by image and regenerate the failures with a
reinforced prompt. In a 60-image set, expect to redo 5–10. Skipping this
step is immediately visible in your reviews.

## 4. Never let the AI render text

AI still mangles lettering. For products that need labels or titles — menu
templates, cards — **generate only the artwork with AI and set the type
yourself** in a design tool. You get to choose real fonts, and the result is
cleaner than any AI text. While you are at it, check that text never
overlaps the artwork; I had enough overlap accidents that I turned the check
into a mandatory rule.

## 5. Disclose AI use

Platforms increasingly require disclosure of AI-generated content — Etsy
already asks in the listing flow. **What you gain by hiding it is trivial
compared to what you lose when caught: the account.** One sentence in the
product description is enough.

## The takeaway

Generation is only the first step. Style lock → transparency post-work →
full manual inspection → typesetting → disclosure is what turns output into
a product. And precisely because most people skip that pipeline, doing it
properly *is* the competitive edge.

---
_Posts on this blog are based on first-hand experience. Some images are
produced with the help of AI tools, and we disclose AI use on our products._
