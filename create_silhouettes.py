from PIL import Image, ImageDraw
import os

out_dir = os.path.join(os.path.dirname(__file__), 'assets', 'silhouettes')
os.makedirs(out_dir, exist_ok=True)

# cat silhouette (simple shape)
cat = Image.new('RGBA', (800, 800), (0,0,0,0))
d = ImageDraw.Draw(cat)
# body
d.ellipse((150, 300, 650, 700), fill=(0,0,0,255))
# head
d.ellipse((260, 150, 540, 420), fill=(0,0,0,255))
# ears
d.polygon([(260,210),(200,120),(320,170)], fill=(0,0,0,255))
d.polygon([(540,210),(600,120),(480,170)], fill=(0,0,0,255))
cat.save(os.path.join(out_dir, 'cat.png'))

# kiwi silhouette (simple body + beak)
kiwi = Image.new('RGBA', (800, 800), (0,0,0,0))
d = ImageDraw.Draw(kiwi)
d.ellipse((180,280,620,540), fill=(0,0,0,255))  # body
d.ellipse((280,200,500,420), fill=(0,0,0,255))  # head overlap
d.rectangle((560,360,700,380), fill=(0,0,0,255))  # beak base
d.polygon([(700,370),(760,360),(700,380)], fill=(0,0,0,255))  # beak tip
kiwi.save(os.path.join(out_dir, 'kiwi.png'))

print("Silhouettes created in assets/silhouettes/")
