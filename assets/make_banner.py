from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
img = Image.new("RGB", (W, H), "#0A0C12")
d = ImageDraw.Draw(img)

# Subtelny pionowy gradient tła
top, bot = (18, 23, 34), (7, 9, 14)
for y in range(H):
    t = y / H
    c = tuple(int(top[i] * (1 - t) + bot[i] * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=c)

# Ciepła poświata z lewej
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for i in range(70, 0, -1):
    a = int(13 * (i / 70))
    gd.ellipse([-360 - i * 8, H // 2 - i * 10, -360 + i * 8, H // 2 + i * 10],
               fill=(212, 168, 83, a))
img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
d = ImageDraw.Draw(img)

# Fonty (Ubuntu Sans variable)
VF = "/usr/share/fonts/truetype/ubuntu/UbuntuSans[wdth,wght].ttf"
def vfont(size, weight):
    f = ImageFont.truetype(VF, size)
    try:
        f.set_variation_by_axes([100, weight])
    except Exception:
        pass
    return f

title_f  = vfont(104, 800)   # META ADS
title2_f = vfont(104, 800)   # DESIGNER
eyeb_f   = vfont(22, 500)
tag_f    = vfont(30, 700)
sub_f    = vfont(20, 400)
foot_f   = vfont(17, 400)
gold     = (212, 168, 83)
white    = (245, 245, 247)
muted    = (140, 148, 160)
dark     = (95, 103, 116)

def tw(f, s):
    return d.textlength(s, font=f)

# --- Lewa kolumna (branding) ---
x0 = 84
# Eyebrow + złota linia
d.text((x0, 66), "THE VISUAL ADVERTISING ENGINE FOR AI AGENTS", font=eyeb_f, fill=muted)
d.rectangle([x0, 106, x0 + 150, 109], fill=gold)

# Tytuł
d.text((x0, 150), "META ADS", font=title_f, fill=white)
d.text((x0, 300), "DESIGNER", font=title2_f, fill=white)

# Złota linia akcentu
d.rectangle([x0, 462, x0 + 330, 465], fill=gold)

# Tagline
d.text((x0, 488), "DON'T DECORATE.  DIRECT.", font=tag_f, fill=gold)

# Stopka
d.text((x0, H - 50), "AI EVOLUTION LABS  ·  CHANNEL ISLANDS", font=foot_f, fill=dark)
url = "github.com/aievolutionpl/meta-ads-designer"
d.text((W - 40 - tw(foot_f, url), H - 50), url, font=foot_f, fill=dark)

# --- Prawe skrzydło: motyw ad-frame (portrety 4:5) ---
# Ramki jako zarysy formatów reklam — czytelne dla "ad designer"
frame_col = (120, 130, 148)
frame_x = 760
f0y, f1y = 92, 178
fw, fh = 118, 148
# Karta główna 4:5
d.rectangle([frame_x, f0y, frame_x + fw, f0y + fh], outline=frame_col, width=2)
d.rectangle([frame_x + 14, f0y + 14, frame_x + fw - 14, f0y + 34], outline=gold, width=1)
# Druga karta (przesunięta, nakładająca się)
d.rectangle([frame_x + 150, f1y, frame_x + 150 + fw, f1y + fh], outline=frame_col, width=2)
d.rectangle([frame_x + 164, f1y + 14, frame_x + 150 + fw - 14, f1y + 34], outline=gold, width=1)
# Trzecia, mniejsza
d.rectangle([frame_x + 315, 128, frame_x + 315 + fw - 20, 128 + fh - 24], outline=frame_col, width=2)

# Podpis pod kartami
cap = "4:5 · 1080×1350 — FEED DEFAULT"
d.text((frame_x, 392), cap, font=eyeb_f, fill=dark)

out = "/home/aibot/repos/premium-ad-design/assets/meta-ads-designer-banner.png"
img.save(out)
print("saved", out, img.size)
