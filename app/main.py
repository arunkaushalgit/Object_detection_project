import streamlit as st
from PIL import Image
import numpy as np
import cv2
import tempfile
import sys
import os

# Add root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inference.visualization import detect_objects, draw_boxes, model

# from inference.visualization import detect_objects, draw_boxes , model # <-- 🔗 Use modular code

st.set_page_config(page_title="YOLOv8 Detection", layout="wide")

st.title("Object Detection App")
st.markdown("Detect objects from **Image**, **Video**, or **Webcam**.")

# Sidebar Settings
st.sidebar.title("⚙️ Settings")
conf_threshold = st.sidebar.slider("Confidence Threshold", 0.1, 1.0, 0.5, 0.05)
mode = st.sidebar.radio("Select Mode", ["Image", "Video", "Webcam"])

# Image Mode
if mode == "Image":
    uploaded_file = st.sidebar.file_uploader("📤 Upload Image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        img_np = np.array(image)

        results = detect_objects(img_np, conf=conf_threshold)
        img_draw, detections = draw_boxes(img_np, results)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🖼️ Original Image")
            st.image(image, use_container_width=True)
        with col2:
            st.subheader("🎯 Detected Image")
            st.image(img_draw, use_container_width=True)

        if detections:
            st.markdown("### 📊 Detection Summary")
            st.dataframe(detections, use_container_width=True)
        else:
            st.info("No objects detected.")

# Video Mode
elif mode == "Video":
    uploaded_video = st.sidebar.file_uploader("📤 Upload Video", type=["mp4", "avi", "mov"])
    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())

        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()
        st.markdown("### 📽️ Processing Video...")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame, conf=conf_threshold)[0]
            img_draw, _ = draw_boxes(frame, results)
            img_rgb = cv2.cvtColor(img_draw, cv2.COLOR_BGR2RGB)
            stframe.image(img_rgb, channels="RGB", use_container_width=True)

        cap.release()

# Webcam Mode
elif mode == "Webcam":
    stframe = st.empty()
    st.markdown("### 🎥 Live Webcam Detection")

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            st.warning("⚠️ Webcam not accessible.")
            break

        results = model(frame, conf=conf_threshold)[0]
        img_draw, _ = draw_boxes(frame, results)
        img_rgb = cv2.cvtColor(img_draw, cv2.COLOR_BGR2RGB)
        stframe.image(img_rgb, channels="RGB", use_container_width=True)

        # if st.sidebar.button("🔴 Stop Webcam"):
        #     break

    cap.release()
