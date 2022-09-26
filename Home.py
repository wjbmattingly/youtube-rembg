import streamlit as st
from rembg import remove
from PIL import Image
import numpy as np

st.title("rembg Demo")
col1, col2 = st.columns(2)
image = st.sidebar.file_uploader("Load Image")
if image:
    with Image.open(image) as img:
        col1.header("Original")
        col1.image(img)

        output = remove(img)
        col2.header("Extracted")
        col2.image(output)
