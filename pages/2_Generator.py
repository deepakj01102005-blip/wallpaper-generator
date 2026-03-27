import streamlit as st
import random
import os
from PIL import Image
from datetime import datetime
from generator.renderer import render_wallpaper
from openai import OpenAI

st.set_page_config(layout="centered")

# -------- OPENAI --------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------- SESSION ----------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------- TITLE ----------
st.markdown("<h1 style='text-align:center;'>✨ Generate Wallpaper</h1>", unsafe_allow_html=True)

# ---------- CONTROLS ----------
category = st.selectbox(
    "🎨 Choose vibe",
    ["Any", "Rain City", "Night Street", "Neon Window", "Fog Forest", "Autumn Path"]
)

CATEGORY_MAP = {
    "Any": "any",
    "Rain City": "rain_city",
    "Night Street": "night_street",
    "Neon Window": "neon_window",
    "Fog Forest": "fog_forest",
    "Autumn Path": "autumn_path"
}
selected_category = CATEGORY_MAP[category]

quote_style = st.selectbox(
    "✍️ Quote style",
    ["Bottom", "Center", "Minimal", "None"]
)

QUOTE_STYLE_MAP = {
    "Bottom": "bottom",
    "Center": "center",
    "Minimal": "minimal",
    "None": "none"
}
selected_quote_style = QUOTE_STYLE_MAP[quote_style]

size_option = st.radio("📐 Size", ["Phone", "Desktop"], horizontal=True)
selected_size = (1080, 1920) if size_option == "Phone" else (1920, 1080)

# ---------- AI + SMART FALLBACK ----------
def generate_ai_quote(mood):
    try:
        prompt = f"Generate a short cinematic aesthetic quote for a {mood} wallpaper. Keep it under 10 words."

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        return response.output_text.strip()

    except Exception:
        scenes = {
            "rain_city": ["rain", "wet streets", "neon reflections"],
            "night_street": ["midnight road", "empty street", "dim lights"],
            "neon_window": ["neon glow", "city lights", "window reflections"],
            "fog_forest": ["misty trees", "quiet forest", "hidden path"],
            "autumn_path": ["falling leaves", "golden path", "soft sunlight"],
            "any": ["still moment", "soft light", "quiet world"]
        }

        emotions = [
            "silence speaks",
            "time slows",
            "memories linger",
            "dreams fade",
            "peace settles"
        ]

        templates = [
            "{scene} where {emotion}.",
            "In the {scene}, {emotion}.",
            "{emotion} within the {scene}."
        ]

        scene = random.choice(scenes.get(mood, scenes["any"]))
        emotion = random.choice(emotions)
        template = random.choice(templates)

        return template.format(scene=scene, emotion=emotion)

# ---------- GENERATE ----------
if st.button("✨ Create Wallpaper", use_container_width=True):

    with st.spinner("🤖 Generating cinematic quote..."):
        quote = generate_ai_quote(category)

    with st.spinner("🎨 Rendering wallpaper..."):
        path = render_wallpaper(
            size=selected_size,
            output_dir="output",
            quote=quote,
            category=selected_category,
            quote_style=selected_quote_style
        )

    # ---------- DISPLAY ----------
    st.image(Image.open(path), use_container_width=True)
    st.markdown(f"💬 *{quote}*")

    # ---------- METADATA ----------
    st.markdown("### 📊 Wallpaper Details")
    st.write(f"**Mood:** {category}")
    st.write(f"**Quote Style:** {quote_style}")
    st.write(f"**Resolution:** {selected_size[0]} x {selected_size[1]}")
    current_time = datetime.now().strftime('%H:%M:%S')
    st.write(f"**Generated At:** {current_time}")

    # ---------- SAVE HISTORY ----------
    st.session_state.history.insert(0, {
        "image": path,
        "quote": quote,
        "time": current_time
    })

    st.session_state.history = st.session_state.history[:5]

    # ---------- DOWNLOAD ----------
    with open(path, "rb") as f:
        st.download_button(
            "⬇️ Download Wallpaper",
            f,
            file_name=os.path.basename(path),
            mime="image/png",
            use_container_width=True
        )

# ---------- HISTORY ----------
if st.session_state.history:

    st.markdown("---")
    col1, col2 = st.columns([8, 2])

    with col1:
        st.markdown("## 🕘 Recent Wallpapers")

    with col2:
        if st.button("🗑️ Clear"):
            st.session_state.history = []
            st.rerun()

    for item in st.session_state.history:

        st.image(Image.open(item["image"]), width=200)
        st.markdown(f"💬 *{item['quote']}*")
        st.markdown(f"🕒 {item['time']}")

        # ---------- DOWNLOAD AGAIN ----------
        with open(item["image"], "rb") as f:
            st.download_button(
                "⬇️ Download Again",
                f,
                file_name=os.path.basename(item["image"]),
                mime="image/png"
            )

        st.markdown("---")