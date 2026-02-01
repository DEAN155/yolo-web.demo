import streamlit as st
st.write("YOLO目标检测工具")
from ultralytics import solutions

inf = solutions.Inference(
    model="yolo11n.pt",
)

inf.inference()