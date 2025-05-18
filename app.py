import streamlit as st
from PIL import Image
import numpy as np
import cv2

from convert import convert_page
from point_transform import point_transform_page
from noise_filters import noise_filters_page
from local_transform import local_transform_page
from edge_detection import edge_detection_page
from global_transform import global_transform_page
from morphology import morphology_page




# --- HIDE Streamlit top-right menu, deploy, gear, footer, etc. ---
st.set_page_config(page_title="Digital Image Processing GUI", layout="wide")
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    .st-emotion-cache-18ni7ap {display: none;}
    .css-1lsmgbg.egzxvld1 {display: none !important;}
    .st-emotion-cache-6qob1r {display: none;}
    .viewerBadge_container__1QSob {display: none !important;}
    .css-164nlkn.egzxvld1 {display: none !important;}
    .block-container {padding-top: 1rem;}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='color:darkred;'>Digital Image Processing Tool</h1>", unsafe_allow_html=True)

def load_image(uploaded_file):
    if uploaded_file is not None:
        image = np.array(Image.open(uploaded_file))
        if image.ndim == 3 and image.shape[2] == 4:
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        if image.ndim == 3:
            return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        else:
            return image
    return None

def print_button():
    st.markdown("""
        <style>
        .print-button {
            background-color: #f63366;
            color: white;
            border: none;
            padding: 0.5rem 1.5rem;
            border-radius: 8px;
            font-size: 1.1rem;
            margin-bottom: 1rem;
            cursor: pointer;
        }
        </style>
        <button class="print-button" onclick="window.print()">🖨️ Print</button>
        """, unsafe_allow_html=True)

# Sidebar for image upload & menu
st.sidebar.title("Upload Image")
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["png", "jpg", "jpeg", "bmp"])
img = load_image(uploaded_file) if uploaded_file else None

st.sidebar.markdown("---")
section = st.sidebar.radio(
    "Select Operation", [
        "Convert",
        "1. Point Transforms",
        "2. Noise & Filters",
        "3. Local Transform Op's",
        "4. Edge Detection",
        "5. Global Transform Op's",
        "6. Morphological Op's"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Made by Ragdha Ali Elgaidi")

# --- Print button at the top of every operation page ---
print_button()

# Main logic for each section
if section == "Convert":
    convert_page(img)
elif section == "1. Point Transforms":
    point_transform_page(img)
elif section == "2. Noise & Filters":
    noise_filters_page(img)
elif section == "3. Local Transform Op's":
    local_transform_page(img)
elif section == "4. Edge Detection":
    edge_detection_page(img)
elif section == "5. Global Transform Op's":
    global_transform_page(img)
elif section == "6. Morphological Op's":
    morphology_page(img)
else:
    st.info("Select an operation from the sidebar.")
