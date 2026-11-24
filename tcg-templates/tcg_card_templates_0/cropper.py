from PIL import Image
import os
import sys

INPUT_DIR = "/home/dave/Documents/Blender/renders/CardTemplate/renders"
OUTPUT_BASE = "/home/dave/Documents/Blender/renders/CardTemplate/renders/cropped"

# Zone name -> (left, top, width, height)
ZONES = {
    "cost":          (78,   75,   235, 225),
    "title":         (394,  75,   730, 147),
    "top_right":     (1130, 75,   312, 199),
    "name_bar":      (138,  1151, 1248, 170),
    "bottom_left":   (96,   1803, 316, 212),
    "bottom_center": (432,  1845, 652, 170),
    "bottom_right":  (1100, 1807, 321, 208),
}

def crop_image(path):
    img = Image.open(path)
    stem = os.path.splitext(os.path.basename(path))[0]
    out_dir = os.path.join(OUTPUT_BASE, stem)
    os.makedirs(out_dir, exist_ok=True)

    for name, (l, t, w, h) in ZONES.items():
        crop = img.crop((l, t, l + w, t + h))
        crop.save(os.path.join(out_dir, f"{name}.png"))
        print(f"{stem}/{name}.png")

paths = [os.path.join(INPUT_DIR, f) for f in os.listdir(INPUT_DIR) if f.endswith('.png')]
for p in paths:
    crop_image(p)

print("Done.")