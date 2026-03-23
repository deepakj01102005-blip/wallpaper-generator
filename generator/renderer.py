import os
import random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import textwrap


def render_wallpaper(size, output_dir, quote, category, quote_style):

    base_path = "assets/photos"

    # ---------- BACKGROUND ----------
    if category == "any":
        folders = [
            f for f in os.listdir(base_path)
            if os.path.isdir(os.path.join(base_path, f))
        ]
        folder = random.choice(folders)
    else:
        folder = category

    folder_path = os.path.join(base_path, folder)
    images = os.listdir(folder_path)
    img_path = os.path.join(folder_path, random.choice(images))

    image = Image.open(img_path).convert("RGB")
    image = image.resize(size)

    draw = ImageDraw.Draw(image)

    # ---------- FONT (FIXED BIG TEXT) ----------
    width, height = size

    # Dynamic font size
    if len(quote) <= 25:
        font_size = int(width * 0.07)
    elif len(quote) <= 60:
        font_size = int(width * 0.05)
    else:
        font_size = int(width * 0.04)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype(
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                font_size
            )
        except:
            font = ImageFont.load_default()

    # ---------- DRAW QUOTE ----------
    if quote_style != "none":

        # Wrap text (better width control)
        wrap_width = 25 if width < 1000 else 40
        wrapped_text = textwrap.fill(quote, width=wrap_width)
        lines = wrapped_text.split("\n")

        # Calculate line height safely
        bbox = draw.textbbox((0, 0), "Ay", font=font)
        line_height = (bbox[3] - bbox[1]) + 10

        total_height = line_height * len(lines)

        # ---------- POSITION ----------
        if quote_style == "center":
            y = (height - total_height) // 2
        elif quote_style == "minimal":
            y = height - total_height - 40
        else:  # bottom
            y = height - total_height - 80

        # ---------- DRAW EACH LINE ----------
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font)
            text_width = bbox[2] - bbox[0]

            x = (width - text_width) // 2

            # Shadow
            draw.text((x + 2, y + 2), line, fill=(0, 0, 0), font=font)

            # Main text
            draw.text((x, y), line, fill=(255, 255, 255), font=font)

            y += line_height

    # ---------- SAVE ----------
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"wallpaper_{timestamp}.png")

    image.save(output_path)

    return output_path