import os
import random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import textwrap


def render_wallpaper(size, output_dir, quote, category, quote_style):
    base_path = "assets/photos"

    # ---------- HANDLE CATEGORY ----------
    if category == "any":
        folders = [
            f for f in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, f))
        ]
        folder = random.choice(folders)
    else:
        folder = category

    folder_path = os.path.join(base_path, folder)

    # ---------- LOAD IMAGE ----------
    images = [
        img for img in os.listdir(folder_path)
        if img.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    if not images:
        raise Exception("No images found in folder")

    image_path = os.path.join(folder_path, random.choice(images))
    image = Image.open(image_path).convert("RGB")
    image = image.resize(size)

    draw = ImageDraw.Draw(image)

    # ---------- FONT ----------
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    # ---------- DRAW QUOTE ----------
    if quote_style != "none":

        # wrap text
        wrapped_text = textwrap.fill(quote, width=25)
        lines = wrapped_text.split("\n")

        line_height = font.size + 10
        total_height = line_height * len(lines)

        # vertical positioning
        if quote_style == "center":
            y = (size[1] - total_height) // 2
        elif quote_style == "minimal":
            y = size[1] - total_height - 40
        else:  # bottom
            y = size[1] - total_height - 80

        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font)
            text_width = bbox[2] - bbox[0]

            x = (size[0] - text_width) // 2

            # shadow
            draw.text((x + 2, y + 2), line, fill=(0, 0, 0), font=font)

            # text
            draw.text((x, y), line, fill=(255, 255, 255), font=font)

            y += line_height

    # ---------- SAVE (FIXED HISTORY BUG) ----------
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"wallpaper_{timestamp}.png")

    image.save(output_path)

    return output_path