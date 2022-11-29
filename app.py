import time
import streamlit as st
import io
from PIL import Image
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

st.title("NutriScan🔍")

ingredients_img = st.file_uploader("Scan the ingredients", type=[
    'jpg', 'jpeg', 'png'], help="Upload an image in jpg, jpeg, png format", accept_multiple_files=False,)

if ingredients_img is not None:
    bytes_data = ingredients_img.getvalue()
    ing_dis_img = Image.open(io.BytesIO(bytes_data))
    st.write("Ingredient Image")
    st.image(ing_dis_img)
    reader = easyocr.Reader(['en'])
    result_ing = reader.readtext(bytes_data, detail=0)
    st.write(result_ing)

    table_img = st.file_uploader("Scan the nutritonal table", type=[
        'jpg', 'jpeg', 'png'], help="Upload an image in jpg, jpeg, png format", accept_multiple_files=False,)

    if table_img is not None:
        bytes_data = table_img.getvalue()
        tab_dis_img = Image.open(io.BytesIO(bytes_data))
        st.write("Table Image")
        st.image(tab_dis_img)
        reader = easyocr.Reader(['en'])
        result_tab = reader.readtext(bytes_data, detail=0)
        st.write(result_tab)

        col1, col2, col3 = st.columns(3)
        col1.metric("Product", "Sodium")
        col2.metric("Content", "800mg")
        col3.metric("Percentage", "86%")

        my_bar = st.progress(0)

        for percent_complete in range(86):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)

        st.info('The verdict says eatable', icon="⚖️")

        with st.expander("❌ Maltodextrin"):
            st.write("""
                Description\n\n Maltodextrin has an even higher glycemic index (GI) than table sugar. This means that maltodextrin can cause a sharp increase, or spike, in people’s blood sugar shortly after they eat foods that contain it.\n\n Side Effects\n\n can increase a person’s risk of high cholesterol, weight gain, and type 2 diabetes.
            """)
        with st.expander("✅ Maltodextrin"):
            st.write("""
                Description\n\n Maltodextrin has an even higher glycemic index (GI) than table sugar. This means that maltodextrin can cause a sharp increase, or spike, in people’s blood sugar shortly after they eat foods that contain it.\n\n Side Effects\n\n can increase a person’s risk of high cholesterol, weight gain, and type 2 diabetes.
            """)