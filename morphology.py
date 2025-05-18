import streamlit as st
import cv2
import numpy as np
from utils import show_img

def morphology_page(img):
    st.header("🟤 Morphological Op's")
    if img is not None:
        # Kernel type selection
        kernel_type = st.selectbox("Choose type of Kernel:", ["arbitrary", "rect", "ellipse", "cross"])
        ksize = st.slider("Kernel Size", 3, 15, 5, step=2)

        # Build kernel
        if kernel_type == "rect":
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize, ksize))
        elif kernel_type == "ellipse":
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ksize, ksize))
        elif kernel_type == "cross":
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (ksize, ksize))
        else:
            # arbitrary: user-defined, default to all-ones
            kernel = np.ones((ksize, ksize), np.uint8)

        col1, col2 = st.columns([2, 1])

        with col1:
            if st.button("Dilation"):
                result = cv2.dilate(img, kernel, iterations=1)
                show_img(result, "Dilation")

            if st.button("Erosion"):
                result = cv2.erode(img, kernel, iterations=1)
                show_img(result, "Erosion")

            if st.button("Close"):
                result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
                show_img(result, "Closing")

            if st.button("Open"):
                result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
                show_img(result, "Opening")
        with col2:
            st.markdown(f"<br><br><b>Choose type of Kernel:</b>", unsafe_allow_html=True)
            # The kernel dropdown is shown above
    else:
        st.info("Upload a grayscale image to begin.")
