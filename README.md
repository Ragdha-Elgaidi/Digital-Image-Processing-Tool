# DIP Lab – Digital Image Processing Studio
----

## 🎯 Purpose

The DIP Lab – Digital Image Processing Studio is designed as an educational and interactive environment, enabling users to explore and apply digital image processing techniques intuitively. By leveraging the simplicity and interactivity of a web-based GUI, the project aims to help students, researchers, and practitioners:

 - Understand image processing concepts through hands-on experimentation.
- Apply various filtering and transformation techniques easily without prior coding experience.
- Visualize real-time changes in image characteristics, enhancing learning and comprehension.
- Encourage experimentation and discovery, promoting active learning and problem-solving skills.

This tool is a valuable educational resource, facilitating practical learning experiences in digital image processing courses or independent studies.

---

## 🚀 Features

- **User-friendly Web Interface** (fully customized, no branding)
- **Image Upload** (PNG, JPG, JPEG, BMP)
- **Interactive Workbench** (combine operations interactively)
- **Image Conversion** (grayscale, color spaces)
- **Point Transforms** (brightness, contrast, histogram equalization)
- **Noise & Filters** (Gaussian, median, mean, salt & pepper, Poisson)
- **Local Operations** (Sobel, Prewitt, Laplacian)
- **Edge Detection** (Canny, Sobel, etc.)
- **Global Operations** (Hough lines, circles detection)
- **Morphological Operations** (erosion, dilation, opening, closing)
- **Download Processed Images**

---

## 🎬 Video Demo

▶️ [Watch the Demo Video on Google Drive](https://drive.google.com/file/d/10l7gvlTaauztLmuXOhWCpxVvSygp_xoG/view?usp=sharing)

---

## 📚 Technologies Used

- **Python 3.11**
- **Streamlit** (web-based interactive GUI)
- **OpenCV** (image processing and computer vision)
- **NumPy** (numerical computing)
- **Pillow** (image manipulation)
- **Scikit-Image** (advanced image processing)
- **PyWavelets** (wavelet transforms)
- **Matplotlib** (visualizations)

--------

## 🛠️ Installation & Usage Guide

### 🔸 Requirements

- Python 3.11 (recommended)
- pip (Python package installer)

### 🔸 Installation Steps

**1\. Clone or Download Project**

Place all files in a project folder.

**2\. (Recommended) Create & Activate Virtual Environment**

```sh
python -m venv venv
.\venv\Scripts\activate  # Windows
```
**3\. Install Dependencies**

```sh
pip install --upgrade pip
pip install streamlit opencv-python pillow numpy scikit-image pywavelets matplotlib
```

**4\. Run the Application**

```sh
streamlit run app.py
```
---------------

## 📁 Project Structure

```text
DIP-Lab/
│
├── app.py
├── workbench.py
├── convert.py
├── point_transform.py
├── noise_filters.py
├── local_transform.py
├── edge_detection.py
├── global_transform.py
├── morphology.py
├── utils.py              # Optional utility functions
├── README.md
└── requirements.txt      # Optional but recommended
```
----------

## 👩‍💻 How to Use the App

- **Upload:** Select and upload images via the sidebar.
- **Process:** Choose operations and adjust settings using sliders.
- **Interactive Workbench:** Combine multiple operations interactively.
- **Preview:** Instantly view the results.
- **Download:** Save processed images directly.

---

## ✨ Credits

- Developed by **Ragdha Ali Elgaidi**.
- Intended for educational and academic purposes.

---

