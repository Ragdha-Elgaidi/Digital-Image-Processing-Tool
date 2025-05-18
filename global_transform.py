import streamlit as st
import cv2
import numpy as np
from utils import show_img

def global_transform_page(img):
    st.header("🌐 Global Transform Op's")
    if img is not None:
        st.subheader("Hough Line Detection")
        if st.button("Apply Hough Lines"):
            # Always work on a grayscale version for edge detection
            if len(img.shape) == 3:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            else:
                gray = img
            edges = cv2.Canny(gray, 50, 150)
            lines = cv2.HoughLinesP(edges, 1, np.pi/180, 80, minLineLength=50, maxLineGap=10)
            line_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            if lines is not None:
                for l in lines:
                    x1, y1, x2, y2 = l[0]
                    cv2.line(line_img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            show_img(line_img, "Hough Lines")

        st.markdown("---")
        st.subheader("Hough Circle Detection")
        min_dist = st.slider("Min distance between centers", 10, 100, 30)
        param1 = st.slider("Canny high threshold", 10, 200, 50)
        param2 = st.slider("Accumulator threshold", 10, 100, 30)
        min_radius = st.slider("Min radius", 1, 100, 10)
        max_radius = st.slider("Max radius", 10, 150, 80)

        if st.button("Apply Hough Circles"):
            # Always convert to grayscale for HoughCircles
            if len(img.shape) == 3:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            else:
                gray = img
            blur = cv2.medianBlur(gray, 5)
            circles = cv2.HoughCircles(
                blur, cv2.HOUGH_GRADIENT, dp=1.2, minDist=min_dist,
                param1=param1, param2=param2,
                minRadius=min_radius, maxRadius=max_radius
            )
            circ_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0, :]:
                    cv2.circle(circ_img, (i[0], i[1]), i[2], (0, 255, 0), 2)
                    cv2.circle(circ_img, (i[0], i[1]), 2, (0, 0, 255), 3)
            show_img(circ_img, "Hough Circles")
    else:
        st.info("Upload an image to begin.")
