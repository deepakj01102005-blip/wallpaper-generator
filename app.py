import streamlit as st

st.set_page_config(page_title="Wallpaper Studio", layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0f1a, #050507);
}

[data-testid="stSidebar"] {
    background: #0a0a0f;
}

.title {
    font-size: 48px;
    font-weight: bold;
}

.subtitle {
    font-size: 18px;
    opacity: 0.7;
}

.section {
    padding: 2rem;
    border-radius: 15px;
    background: rgba(255,255,255,0.05);
    margin-top: 2rem;
}

.stButton>button {
    background: linear-gradient(135deg, #7c3aed, #4f46e5);
    color: white;
    border-radius: 10px;
    border: none;
    height: 3em;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown('<p class="title"><h1>🎨 Wallpaper Studio</h1></p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Generate aesthetic wallpapers based on your mood</p>', unsafe_allow_html=True)

st.divider()

st.markdown("## 🌄 Preview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee", use_container_width=True)

with col2:
    st.image("https://images.unsplash.com/photo-1575657695080-a5a861859078?q=80&w=387&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", use_container_width=True)

with col3:
    st.image("https://plus.unsplash.com/premium_photo-1668967516060-624b8a7021f4?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8YXV0dW1ufGVufDB8fDB8fHww", use_container_width=True)

with col4:
    st.image("https://images.unsplash.com/photo-1543518360-68b9612a7c8c?q=80&w=387&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", use_container_width=True)

st.divider()
# ---------- MAIN SECTION ----------
col1, col2 = st.columns(2)

with col1:
    
    st.markdown("### 🎭 Explore Moods")
    st.write("Browse different aesthetic styles")

    if st.button("Open Moods"):
        st.switch_page("pages/1_Moods.py")

    

with col2:
   
    st.markdown("### ⚡ Generate Wallpaper")
    st.write("Create your own wallpaper instantly")

    if st.button("Start Generating"):
        st.switch_page("pages/2_Generator.py")

   

st.divider()
