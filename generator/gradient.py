from PIL import Image
import numpy as np
import random

def random_gradient(size, palette):
    w, h = size
    angle = random.choice(["vertical", "horizontal", "diagonal"])

    base = np.zeros((h, w, 3), dtype=np.uint8)
    c1, c2 = random.sample(palette, 2)

    for y in range(h):
        for x in range(w):
            if angle == "vertical":
                t = y / h
            elif angle == "horizontal":
                t = x / w
            else:
                t = (x + y) / (w + h)

            base[y, x] = [
                int(c1[i] * (1 - t) + c2[i] * t) for i in range(3)
            ]

    return Image.fromarray(base)
