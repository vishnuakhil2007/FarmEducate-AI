import base64
import os
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="FarmEducate AI", 
    page_icon="🌾",
    layout="wide"
)

# Function to convert local image file to base64 string for CSS background
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

banner_b64 = get_base64_image("farmer_banner.png")

# Dynamic CSS Header Background
if banner_b64:
    banner_css = f"background-image: linear-gradient(rgba(0, 0, 0, 0.35), rgba(0, 0, 0, 0.55)), url('data:image/png;base64,{banner_b64}');"
else:
    banner_css = "background: linear-gradient(135deg, #0288D1 0%, #0097A7 40%, #2E7D32 100%);"

# Clean, Modern Styling (Restoring Plus Jakarta Sans & Blue/Green Palette)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}

    /* Main Header with Base64 Background Image */
    .hero-banner {{
        {banner_css}
        background-size: cover;
        background-position: center 30%;
        padding: 4rem 2rem 3.5rem 2rem;
        border-radius: 18px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 12px 30px rgba(2, 136, 209, 0.25);
    }}

    .hero-title {{
        color: #FFFFFF !important;
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 0.5rem;
        text-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    }}

    .hero-subtitle {{
        color: #E0F7FA !important;
        font-size: 1.25rem;
        font-weight: 500;
        text-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
        margin: 0;
    }}

    /* Glassmorphism Input Cards */
    .modern-card {{
        background: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-radius: 14px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.04);
    }}

    /* Water & Green Parameter Box */
    .param-badge {{
        background: #E1F5FE;
        border-left: 5px solid #0288D1;
        padding: 1.2rem;
        border-radius: 10px;
        color: #01579B;
        font-size: 1rem;
        line-height: 1.8;
    }}

    .param-item {{
        display: flex;
        justify-content: space-between;
        border-bottom: 1px solid #B3E5FC;
        padding-bottom: 0.3rem;
        margin-bottom: 0.4rem;
    }}

    .param-item b {{
        color: #0277BD;
    }}

    /* Modern Primary Action Button */
    div.stButton > button {{
        background: linear-gradient(135deg, #0288D1 0%, #2E7D32 100%) !important;
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        padding: 0.75rem 2rem !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 6px 18px rgba(2, 136, 209, 0.3) !important;
        width: 100%;
        transition: all 0.2s ease !important;
    }}

    div.stButton > button:hover {{
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 22px rgba(2, 136, 209, 0.4) !important;
    }}
    </style>
""", unsafe_allow_html=True)

# 1. Hero Header
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">🌾 FarmEducate AI 💧</h1>
        <p class="hero-subtitle">Generative Visual Engine for AgTech, Irrigation & Crop Education</p>
    </div>
""", unsafe_allow_html=True)

# 2. Sidebar Parameters
with st.sidebar:
    st.header("⚙️ Studio Settings")
    
    region = st.selectbox(
        "📍 Target Region",
        ["Telangana / Andhra Pradesh", "Punjab / Haryana", "Maharashtra", "Karnataka", "Tamil Nadu", "General / International"]
    )
    
    crop_type = st.selectbox(
        "🌾 Crop Stage",
        ["Dense Green Paddy / Rice", "Well-Grown Maize", "Blooming Cotton", "Wheat Field", "Sugarcane", "Vegetables & Foliage"]
    )
    
    water_source = st.selectbox(
        "💧 Irrigation Context",
        ["Muddy Canal / Flooded Path", "Precision Drip Line", "Rainfed / Monsoon Soil", "Solar Borewell Pump"]
    )
    
    fertilizer_type = st.selectbox(
        "🌱 Activity Stage",
        ["Hand-broadcasting NPK granules", "Organic compost dusting", "Urea hand-scattering", "Liquid foliar spray"]
    )
    
    visual_style = st.radio(
        "🎨 Visual Output Style",
        ["Photorealistic Field Photo", "Infographic Vector Diagram", "3D Render"]
    )

    st.markdown("---")
    st.caption("FarmEducate AI v3.0 • Modern AgTech Edition")

# 3. Main Workspace Area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="modern-card">', unsafe_allow_html=True)
    st.subheader("💡 Visual Prompt Builder")
    
    st.write("<b>Quick Scenario Presets:</b>", unsafe_allow_html=True)
    p1, p2, p3 = st.columns(3)
    preset_prompt = ""
    
    if p1.button("🌾 Broadcast Fertilizer", use_container_width=True):
        preset_prompt = "A smiling farmer broadcasting granular fertilizer into a lush green rice field along a muddy flooded track with a tractor in early morning light"
    if p2.button("💧 Drip Line Setup", use_container_width=True):
        preset_prompt = "Close-up macro photo of a drip irrigation system watering cotton crop roots at sunrise, water droplets glistening"
    if p3.button("☀️ Solar Pump Field", use_container_width=True):
        preset_prompt = "Solar-powered water pump irrigating lush green agricultural fields during bright morning sunlight"

    user_prompt = st.text_area(
        "Describe the visual concept:",
        value=preset_prompt,
        placeholder="e.g., A happy farmer scattering fertilizer in a well-grown paddy field during morning golden hour...",
        height=130
    )
    
    generate_btn = st.button("🚀 Generate Visual", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="modern-card">', unsafe_allow_html=True)
    st.subheader("📊 Selected Context")
    
    st.markdown(f"""
        <div class="param-badge">
            <div class="param-item"><b>📍 Region:</b> <span>{region}</span></div>
            <div class="param-item"><b>🌾 Crop:</b> <span>{crop_type}</span></div>
            <div class="param-item"><b>💧 Water:</b> <span>{water_source}</span></div>
            <div class="param-item"><b>🌱 Activity:</b> <span>{fertilizer_type}</span></div>
            <div class="param-item"><b>🎨 Style:</b> <span>{visual_style}</span></div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 4. Pipeline Execution
if generate_btn:
    if user_prompt:
        st.markdown('<div class="modern-card">', unsafe_allow_html=True)
        st.success(f"Processing Gen AI visual pipeline for **{crop_type}** ({region})...")
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("Step 1/3: Refining description with LLM for regional crop accuracy...")
        progress_bar.progress(33)
        
        status_text.text("Step 2/3: Applying sunrise lighting & water reflection details...")
        progress_bar.progress(66)
        
        status_text.text("Step 3/3: Running Diffusion Engine generation...")
        progress_bar.progress(100)
        
        st.info("Backend AI pipeline integration is ready for Phase 5!")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("Please enter a description or pick a preset scenario first.")