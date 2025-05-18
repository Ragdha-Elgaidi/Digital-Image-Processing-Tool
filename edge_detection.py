import streamlit as st
import cv2
import numpy as np
from skimage.morphology import skeletonize, thin

from utils import show_img

def edge_detection_page(img):
    st.header("🔹 Edge Detection Filters")
    if img is not None:
        # Map UI names to functions
        filter_names = [
            "Laplacian filter",
            "Gaussian filter",
            "Vert. Sobel", "Horiz. Sobel",
            "Vert. Prewitt", "Horiz. Prewitt",
            "Lap of Gau(log)", "Canny method",
            "Zero Cross", "Thicken", "Skeleton", "Thinning"
        ]

        selected = st.radio("Select edge detection filter:", filter_names, horizontal=False)

        result = None

        if selected == "Laplacian filter":
            result = cv2.Laplacian(img, cv2.CV_64F)
            result = np.uint8(np.absolute(result))
        elif selected == "Gaussian filter":
            result = cv2.GaussianBlur(img, (5, 5), 1)
        elif selected == "Vert. Sobel":
            result = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
            result = np.uint8(np.absolute(result))
        elif selected == "Horiz. Sobel":
            result = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
            result = np.uint8(np.absolute(result))
        elif selected == "Vert. Prewitt":
            # Prewitt kernel
            kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
            result = cv2.filter2D(img, -1, kernelx)
        elif selected == "Horiz. Prewitt":
            kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
            result = cv2.filter2D(img, -1, kernely)
        elif selected == "Lap of Gau(log)":
            blur = cv2.GaussianBlur(img, (3, 3), 0)
            result = cv2.Laplacian(blur, cv2.CV_64F)
            result = np.uint8(np.absolute(result))
        elif selected == "Canny method":
            t1 = st.slider("Canny Threshold1", 0, 255, 50)
            t2 = st.slider("Canny Threshold2", 0, 255, 150)
            result = cv2.Canny(img, t1, t2)
        elif selected == "Zero Cross":
            # Zero-crossing: Laplacian then zero crossing
            lap = cv2.Laplacian(img, cv2.CV_64F)
            result = np.zeros_like(lap)
            # Simple zero-crossing detection
            result[(np.roll(lap, 1, axis=0) * lap) < 0] = 255
            result = np.uint8(result)
        elif selected == "Thicken":
            # Morphological "dilation" can be used for thickening
            kernel = np.ones((3, 3), np.uint8)
            result = cv2.dilate(img, kernel, iterations=1)
        elif selected == "Skeleton":
            # Skeletonization with skimage
            bin_img = img > 127
            skeleton = skeletonize(bin_img)
            result = (skeleton * 255).astype(np.uint8)
        elif selected == "Thinning":
            # Thinning with skimage
            bin_img = img > 127
            thin_img = thin(bin_img)
            result = (thin_img * 255).astype(np.uint8)
        else:
            st.info("Select a filter.")

        if result is not None:
            show_img(result, f"{selected} Output")
    else:
        st.info("Upload a grayscale image to begin.")
