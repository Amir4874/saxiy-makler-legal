"""Generate favicon and app-icon variants from master 1024x1024 source."""
from pathlib import Path
from PIL import Image

SRC = Path(r"D:/AI space/Projects/poster/resources/saxiy_makler_1024x1024.jpg")
OUT = Path(r"D:/AI space/Projects/poster-tiktok-legal/assets")
OUT.mkdir(parents=True, exist_ok=True)

img = Image.open(SRC).convert("RGBA")
assert img.size == (1024, 1024), f"Expected 1024x1024, got {img.size}"

targets = [
    ("logo-1024.png", 1024),
    ("logo-512.png", 512),
    ("logo-192.png", 192),
    ("apple-touch-icon.png", 180),
    ("favicon-32.png", 32),
    ("favicon-16.png", 16),
]

for name, size in targets:
    resized = img.resize((size, size), Image.LANCZOS)
    resized.save(OUT / name, format="PNG", optimize=True)
    print(f"  {name}: {size}x{size}")

ico_sizes = [(16, 16), (32, 32), (48, 48)]
img.save(OUT / "favicon.ico", format="ICO", sizes=ico_sizes)
print(f"  favicon.ico: 16+32+48 multi-size")

print(f"\nAll 7 files written to: {OUT}")
