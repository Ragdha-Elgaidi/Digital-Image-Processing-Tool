import streamlit as st
import cv2
import numpy as np
from skimage import util
from utils import show_img

def add_poisson_noise(image):
    # Normalize image to 0-1 if not already
    img = image.astype(np.float32) / 255.0
    # Poisson noise expects values in range [0, 1] or integer counts
    noisy = np.random.poisson(img * 255) / 255.0
    noisy = np.clip(noisy, 0, 1)
    return (noisy * 255).astype(np.uint8)

def noise_filters_page(img):
    st.header("🟤 Noise Models & Filters")
    if img is not None:
        noise_type = st.selectbox("Noise Type", ["Salt & Pepper", "Gaussian", "Poisson"])
        if noise_type == "Salt & Pepper":
            amount = st.slider("S&P Amount", 0.0, 0.2, 0.05)
            noisy = util.random_noise(img, mode='s&p', amount=amount)
            noisy_uint8 = (noisy * 255).astype(np.uint8)
        elif noise_type == "Gaussian":
            var = st.slider("Gaussian Variance", 0.0, 0.05, 0.01)
            noisy = util.random_noise(img, mode='gaussian', var=var)
            noisy_uint8 = (noisy * 255).astype(np.uint8)
        else:  # Poisson
            noisy_uint8 = add_poisson_noise(img)
        show_img(noisy_uint8, f"{noise_type} Noise")

        filter_type = st.selectbox("Filter", ["Mean 3x3", "Gaussian 5x5", "Median 5x5"])
        if filter_type == "Mean 3x3":
            filtered = cv2.blur(noisy_uint8, (3, 3))
        elif filter_type == "Gaussian 5x5":
            filtered = cv2.GaussianBlur(noisy_uint8, (5, 5), 1)
        else:
            filtered = cv2.medianBlur(noisy_uint8, 5)
        show_img(filtered, f"{filter_type} Result")
    else:
        st.info("Upload a grayscale image to begin.")
