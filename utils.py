import numpy as np
import cv2
import streamlit as st

def load_image(uploaded):
    if uploaded is not None:
        file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 0)
        return img
    return None

def show_img(img, caption=""):
    st.image(img, caption=caption, channels="GRAY", use_column_width=True)

def to_grayscale(img):
    if len(img.shape) == 3:
        # Convert BGR (from OpenCV) or RGB to grayscale
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img
