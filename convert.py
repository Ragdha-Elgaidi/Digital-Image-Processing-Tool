import streamlit as st
import cv2
from utils import show_img

def convert_page(img):
    st.header("🎨 Convert")
    if img is not None:
        options = ["Default color", "Gray color"]
        selected = st.radio("Choose conversion type:", options)

        if selected == "Default color":
            # If uploaded image is grayscale, just show as is
            if len(img.shape) == 2:
                out_img = img
                st.info("Image is already grayscale (showing as default).")
            else:
                out_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            show_img(out_img, "Default color image")
        else:  # Gray color
            if len(img.shape) == 2:
                out_img = img  # Already gray
            else:
                out_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            show_img(out_img, "Grayscale image")
    else:
        st.info("Upload an image to begin.")
