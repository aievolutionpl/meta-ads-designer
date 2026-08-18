from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
img = Image.new("RGB", (W, H), "#0B0E14")
d = ImageDraw.Draw(img)

# Subtelny pionowy gradient tła (jaśniej u góry)
top = (22, 27, 38)
bot = (8, 10, 16)
for y in range(H):
    t = y / H
    c = tuple(int(top[i] * (1 - t) + bot[i] * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=c)

# Ciepła poświata z lewej (radial approx — kilka pasów)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
for i in range(60, 0, -1):
    a = int(14 * (i / 60))
    gd.ellipse([-320 - i * 8, H//2 - i * 9, -320 + i * 8, H//2 + i * 9], fill=(212, 168, 83, a))
img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
d = ImageDraw.Draw(img)

def font(path, size):
    return ImageFont.truetype(path, size)

# Fonty
title_f = font("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 96)
tag_f   = font("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 34)
sub_f   = font("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 26)
foot_f  = font("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 18)
small_f = font("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 20)

# Mała etykieta u góry
d.text((90, 52), "THE VISUAL ADVERTISING ENGINE FOR AI AGENTS", font=small_f, fill=(160, 168, 180))
d.rectangle([90, 52 + 34, 210, 55 + 34], fill="#D4A853")

# Tytuł
d.text((86, 190), "META ADS", font=title_f, fill=(255, 255, 255))
d.text((86, 320), "DESIGNER", font=title_f, fill=(255, 255, 255))

# Złota linia akcentu
d.rectangle([90, 505, 470, 508], fill="#D4A853")

# Tagline
d.text((90, 530), "DON'T DECORATE. DIRECT.", font=tag_f, fill=(212, 168, 83))

# Stopka
d.text((90, H - 52), "AI EVOLUTION LABS  ·  CHANNEL ISLANDS", font=foot_f, fill=(120, 128, 140))
d.text((W - 320, H - 52), "github.com/aievolutionpl/meta-ads-designer", font=foot_f, fill=(120, 128, 140))

out = "/home/aibot/repos/premium-ad-design/assets/meta-ads-designer-banner.png"
img.save(out)
print("saved", out, img.size)
