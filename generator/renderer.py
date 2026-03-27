import os
import random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import textwrap


def render_wallpaper(size, output_dir, quote, category, quote_style):

    width, height = size

    # ---------- LOAD IMAGE ----------
    base_path = "assets/photos"

    if category == "any":
        folders = [
            f for f in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, f))
        ]
        folder = random.choice(folders)
    else:
        folder = category

    folder_path = os.path.join(base_path, folder)

    images = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    image_path = os.path.join(folder_path, random.choice(images))

    image = Image.open(image_path).convert("RGB")
    image = image.resize((width, height))

    draw = ImageDraw.Draw(image)

    # ---------- FONT SIZE (FIXED BIG TEXT) ----------
    if len(quote) <= 25:
        font_size = int(width * 0.18)
        print("font sie",font_size)
    elif len(quote) <= 60:
        font_size = int(width * 0.14)
    else:
        font_size = int(width * 0.12)

    # ---------- LOAD FONT ----------
    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            font_size
        )
    except:
        try:
            font = ImageFont.truetype(
                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                font_size
            )
        except:
            font = ImageFont.load_default()

    # ---------- DRAW QUOTE ----------
    if quote_style != "none":

        # 🔥 SMART WRAPPING (MAIN FIX)
        if len(quote) <= 30:
            lines = [quote]   # no wrapping → BIG text
        else:
            wrap_width = 40
            wrapped_text = textwrap.fill(quote, width=wrap_width)
            lines = wrapped_text.split("\n")

        # line height
        bbox = draw.textbbox((0, 0), "Ay", font=font)
        line_height = (bbox[3] - bbox[1]) + 20

        total_height = line_height * len(lines)

        # position
        if quote_style == "center":
            y = (height - total_height) // 2
        elif quote_style == "minimal":
            y = height - total_height - 40
        else:  # bottom
            y = height - total_height - 80

        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font)
            text_width = bbox[2] - bbox[0]

            x = (width - text_width) // 2

            # shadow
            draw.text((x + 3, y + 3), line, fill=(0, 0, 0), font=font)

            # main text
            draw.text((x, y), line, fill=(255, 255, 255), font=font)

            y += line_height

    # ---------- SAVE ----------
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    output_path = os.path.join(output_dir, f"wallpaper_{timestamp}.png")

    image.save(output_path)

    return output_path