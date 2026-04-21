from PIL import Image
import os

src = os.path.join(os.path.dirname(__file__), "images")
dst = os.path.join(os.path.dirname(__file__), "images_compressed")
os.makedirs(dst, exist_ok=True)

MB = 1024 * 1024

for f in sorted(os.listdir(src)):
    if f.endswith(".png"):
        img = Image.open(os.path.join(src, f))
        img = img.convert("RGB")
        w, h = img.size
        if w > 1920:
            ratio = 1920 / w
            img = img.resize((1920, int(h * ratio)), Image.LANCZOS)
        out = os.path.join(dst, f.replace(".png", ".jpg"))
        img.save(out, "JPEG", quality=75, optimize=True)
        orig_size = os.path.getsize(os.path.join(src, f)) / MB
        new_size = os.path.getsize(out) / MB
        print(f"{f}: {orig_size:.1f}MB -> {new_size:.2f}MB")

print("\nDone!")
