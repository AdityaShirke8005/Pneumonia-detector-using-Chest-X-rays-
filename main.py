import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np

from util import classify, set_background


set_background('bg.jpg')

# set title
st.markdown("<h1 style='text-align: center;'>Pneumonia classification</h1>", unsafe_allow_html=True)

st.markdown(
            "<p class='footer' style='text-align: center;'>Created with ❤️ by Aditya Shirke</p>",
            unsafe_allow_html=True
        )

# set header
st.markdown("<h2 style='text-align: center;'>Please upload a chest X-ray image</h2>", unsafe_allow_html=True)

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model = load_model('./model/pneumonia_classifier.h5')

# load class names
with open('./model/labels.txt', 'r') as f:
    class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()

# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    class_name, conf_score = classify(image, model, class_names)

    # write classification
    st.write("## {}".format(class_name))
    st.write("## confidence score: {}%".format(int(conf_score * 1000) / 10))
