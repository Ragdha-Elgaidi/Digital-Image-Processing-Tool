import streamlit as st
import cv2
import numpy as np
from utils import show_img

def point_transform_page(img):
    st.header("⚡ Point Transforms")

    if img is not None:
        st.subheader("Brightness/Contrast Adjustment")
        alpha = st.slider("Contrast (alpha)", 0.5, 3.0, 1.0)
        beta = st.slider("Brightness (beta)", -100, 100, 0)
        if st.button("Apply Brightness/Contrast"):
            adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
            show_img(adjusted, "Brightness/Contrast Adjusted")

        st.markdown("---")
        st.subheader("Histogram Equalization")

        if st.button("Apply Histogram Equalization"):
            # Handle grayscale and color images
            if len(img.shape) == 3 and img.shape[2] == 3:
                # Convert to YCrCb, equalize Y channel only
                ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
                y, cr, cb = cv2.split(ycrcb)
                y_eq = cv2.equalizeHist(y)
                ycrcb_eq = cv2.merge([y_eq, cr, cb])
                eq_img = cv2.cvtColor(ycrcb_eq, cv2.COLOR_YCrCb2BGR)
                show_img(eq_img, "Histogram Equalized (Color)")
            else:
                # Grayscale image
                eq_img = cv2.equalizeHist(img)
                show_img(eq_img, "Histogram Equalized (Grayscale)")
    else:
        st.info("Upload an image to start.")
