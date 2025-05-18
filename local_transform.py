import streamlit as st
import cv2
import numpy as np
from utils import show_img

def local_transform_page(img):
    st.header("🔹 Local Transform Op's")
    if img is not None:
        col1, col2 = st.columns(2)
        # Add buttons
        if col1.button("Low pass filter"):
            # Low pass = Gaussian blur
            result = cv2.GaussianBlur(img, (5, 5), 1)
            show_img(result, "Low pass filter (Gaussian blur)")

        if col2.button("High pass filter"):
            # High pass = sharpened (original - blurred)
            blur = cv2.GaussianBlur(img, (5, 5), 1)
            high_pass = cv2.addWeighted(img, 1.5, blur, -0.5, 0)
            show_img(high_pass, "High pass filter (Sharpened)")

        if col1.button("Median filtering (gray image)"):
            median = cv2.medianBlur(img, 5)
            show_img(median, "Median filtering (5x5)")

        if col2.button("Averaging filtering"):
            mean = cv2.blur(img, (5, 5))
            show_img(mean, "Averaging filter (Mean blur 5x5)")
    else:
        st.info("Upload a grayscale image to begin.")
