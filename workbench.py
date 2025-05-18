'''import streamlit as st
import cv2
import numpy as np
from PIL import Image
from utils import show_img

def workbench_page(img):
    st.header("🧰 Interactive Workbench")
    if img is not None:
        # Use session state to store current working image
        if 'work_img' not in st.session_state or st.button("Reset to Original"):
            st.session_state.work_img = img.copy()

        show_img(st.session_state.work_img, "Current Image")

        st.markdown("---")
        st.subheader("Choose any operation below and click 'Apply'!")

        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
            "Convert", "Point Transform", "Noise", "Local Filter", "Edge Detection", "Morphology", "Global"
        ])

        # Each tab operates on the current image in session_state.work_img
        with tab1:
            option = st.radio("Color conversion", ["Default color", "Gray color"])
            if st.button("Apply Convert", key="conv"):
                if option == "Gray color" and len(st.session_state.work_img.shape) == 3:
                    st.session_state.work_img = cv2.cvtColor(st.session_state.work_img, cv2.COLOR_BGR2GRAY)
                elif option == "Default color" and len(st.session_state.work_img.shape) == 2:
                    st.info("Original color info lost (only grayscale available)")

        with tab2:
            alpha = st.slider("Contrast (alpha)", 0.5, 3.0, 1.0)
            beta = st.slider("Brightness (beta)", -100, 100, 0)
            if st.button("Apply Point Transform", key="point"):
                st.session_state.work_img = cv2.convertScaleAbs(st.session_state.work_img, alpha=alpha, beta=beta)

        with tab3:
            noise_type = st.selectbox("Noise type", ["Salt & Pepper", "Gaussian", "Poisson"])
            if st.button("Apply Noise", key="noise"):
                from skimage import util
                def add_poisson(image):
                    arr = image.astype(np.float32)/255.0
                    noisy = np.random.poisson(arr*255)/255.0
                    return np.clip(noisy*255, 0, 255).astype(np.uint8)
                img2 = st.session_state.work_img
                if noise_type == "Salt & Pepper":
                    amount = st.slider("Amount", 0.0, 0.2, 0.05, key="sp")
                    noisy = util.random_noise(img2, mode='s&p', amount=amount)
                    st.session_state.work_img = (noisy * 255).astype(np.uint8)
                elif noise_type == "Gaussian":
                    var = st.slider("Variance", 0.0, 0.05, 0.01, key="gauss")
                    noisy = util.random_noise(img2, mode='gaussian', var=var)
                    st.session_state.work_img = (noisy * 255).astype(np.uint8)
                else:
                    st.session_state.work_img = add_poisson(img2)

        with tab4:
            ftype = st.selectbox("Filter type", ["Mean", "Median", "Gaussian"])
            if st.button("Apply Local Filter", key="filt"):
                img2 = st.session_state.work_img
                if ftype == "Mean":
                    st.session_state.work_img = cv2.blur(img2, (5,5))
                elif ftype == "Median":
                    st.session_state.work_img = cv2.medianBlur(img2, 5)
                elif ftype == "Gaussian":
                    st.session_state.work_img = cv2.GaussianBlur(img2, (5,5), 1)

        with tab5:
            edge_type = st.selectbox("Edge type", [
                "Laplacian", "Vert. Sobel", "Horiz. Sobel",
                "Vert. Prewitt", "Horiz. Prewitt", "Canny"
            ])
            if st.button("Apply Edge Detection", key="edge"):
                img2 = st.session_state.work_img
                if edge_type == "Laplacian":
                    e = cv2.Laplacian(img2, cv2.CV_64F)
                    st.session_state.work_img = np.uint8(np.abs(e))
                elif edge_type == "Vert. Sobel":
                    e = cv2.Sobel(img2, cv2.CV_64F, 1, 0, ksize=3)
                    st.session_state.work_img = np.uint8(np.abs(e))
                elif edge_type == "Horiz. Sobel":
                    e = cv2.Sobel(img2, cv2.CV_64F, 0, 1, ksize=3)
                    st.session_state.work_img = np.uint8(np.abs(e))
                elif edge_type == "Vert. Prewitt":
                    kernelx = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
                    st.session_state.work_img = cv2.filter2D(img2, -1, kernelx)
                elif edge_type == "Horiz. Prewitt":
                    kernely = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
                    st.session_state.work_img = cv2.filter2D(img2, -1, kernely)
                elif edge_type == "Canny":
                    t1 = st.slider("Canny t1", 0, 255, 50, key="ct1")
                    t2 = st.slider("Canny t2", 0, 255, 150, key="ct2")
                    st.session_state.work_img = cv2.Canny(img2, t1, t2)

        with tab6:
            morph_type = st.selectbox("Morphology", ["Dilation", "Erosion", "Open", "Close"])
            ksize = st.slider("Kernel size", 3, 15, 5, step=2, key="morphk")
            if st.button("Apply Morphology", key="morph"):
                img2 = st.session_state.work_img
                kernel = np.ones((ksize,ksize), np.uint8)
                if morph_type == "Dilation":
                    st.session_state.work_img = cv2.dilate(img2, kernel)
                elif morph_type == "Erosion":
                    st.session_state.work_img = cv2.erode(img2, kernel)
                elif morph_type == "Open":
                    st.session_state.work_img = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)
                elif morph_type == "Close":
                    st.session_state.work_img = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

        with tab7:
            global_type = st.selectbox("Global", ["Hough Lines", "Hough Circles"])
            if st.button("Apply Global", key="global"):
                img2 = st.session_state.work_img
                if global_type == "Hough Lines":
                    edges = cv2.Canny(img2, 50, 150)
                    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 80, minLineLength=50, maxLineGap=10)
                    line_img = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR) if len(img2.shape)==2 else img2.copy()
                    if lines is not None:
                        for l in lines:
                            x1,y1,x2,y2 = l[0]
                            cv2.line(line_img, (x1,y1), (x2,y2), (0,0,255), 2)
                    st.session_state.work_img = line_img
                elif global_type == "Hough Circles":
                    blur = cv2.medianBlur(img2, 5)
                    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.2, 30, param1=50, param2=30, minRadius=10, maxRadius=80)
                    circ_img = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR) if len(img2.shape)==2 else img2.copy()
                    if circles is not None:
                        circles = np.uint16(np.around(circles))
                        for i in circles[0,:]:
                            cv2.circle(circ_img, (i[0],i[1]), i[2], (0,255,0), 2)
                            cv2.circle(circ_img, (i[0],i[1]), 2, (0,0,255), 3)
                    st.session_state.work_img = circ_img

        st.markdown("---")
        if st.button("Download current image"):
            from PIL import Image as PILImage
            im = st.session_state.work_img
            if len(im.shape) == 2:
                im = cv2.cvtColor(im, cv2.COLOR_GRAY2RGB)
            pil_img = PILImage.fromarray(im)
            st.download_button("Download", data=pil_img.tobytes(), file_name="processed.png")

    else:
        st.info("Upload an image to begin.")
'''
import streamlit as st
from PIL import Image
import numpy as np
import cv2

from workbench import workbench_page
from convert import convert_page
from point_transform import point_transform_page
from noise_filters import noise_filters_page
from local_transform import local_transform_page
from edge_detection import edge_detection_page
from global_transform import global_transform_page
from morphology import morphology_page

# Hide Streamlit system UI (deploy, menu, gear, footer, etc)
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

# Print button
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

# Helper to read file as cv2 image
def load_image(uploaded_file):
    if uploaded_file is not None:
        image = np.array(Image.open(uploaded_file))
        # Always convert RGBA to RGB if needed
        if image.ndim == 3 and image.shape[2] == 4:
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        # Convert to BGR for OpenCV functions
        if image.ndim == 3:
            return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        else:
            return image
    return None

# Sidebar for image upload & menu
st.sidebar.title("Upload Image")
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["png", "jpg", "jpeg", "bmp"])
img = load_image(uploaded_file) if uploaded_file else None

st.sidebar.markdown("---")
section = st.sidebar.radio(
    "Select Operation", [
        "Interactive Workbench",
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
if section == "Interactive Workbench":
    workbench_page(img)
elif section == "Convert":
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


