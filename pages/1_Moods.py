import streamlit as st
import os
from PIL import Image

st.set_page_config(layout="wide")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0f1a, #050507);
}

.title {
    color: #7c3aed;
}
</style>
""", unsafe_allow_html=True)

st.title("🎨 Wallpaper Moods")

BASE_PATH = "assets/photos"

MOODS = {
    "Rain City": "rain_city",
    "Night Street": "night_street",
    "Neon Window": "neon_window",
    "Fog Forest": "fog_forest",
    "Autumn Path": "autumn_path"
}

for mood, folder in MOODS.items():
    st.markdown(f"<h2 class='title'>{mood}</h2>", unsafe_allow_html=True)

    images = [
        os.path.join(BASE_PATH, folder, img)
        for img in os.listdir(os.path.join(BASE_PATH, folder))
        if img.lower().endswith((".jpg", ".png", ".jpeg"))
    ]

    cols = st.columns(3)

    for i, img_path in enumerate(images[:3]):
        with cols[i]:
            st.image(Image.open(img_path), use_container_width=True)

    st.divider()