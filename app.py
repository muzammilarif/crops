import cv2
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input

st.title("Crop Analysis")
model = tf.keras.models.load_model("saved_model/fypmodel3.h5")
### load file
uploaded_file = st.file_uploader("Choose a image file", type="jpg")

map_dict = {0: 'Apple scab',
            1: 'Apple Black rot',
            2: 'Apple Cedar apple rust',
            3: 'Apple healthy',
            4: 'Blueberry healthy',
            5: 'Cherry Powdery mildew',
            6: 'Cherry healthy',
            7: 'Corn (maize) Cercospora leaf spot Gray leaf spot',
            8: 'Corn (maize) Common rust ',
            9: 'Corn (maize) Northern Leaf Blight',
            10: 'Corn (maize) healthy',
            11: 'Grape Black rot',
            12: 'Grape Esca (Black Measles)',
            13: 'Grape Leaf blight (Isariopsis Leaf Spot)',
            14: 'Grape healthy',
            15: 'Orange Haunglongbing (Citrus greening)',
            16: 'Peach Bacterial spot',
            17: 'Peach healthy',
            18: 'Pepper, bell Bacterial spot',
            19: 'Pepper, bell healthy',
            20: 'Potato Early blight',
            21: 'Potato Late blight',
            22: 'Potato healthy',
            23: 'Raspberry healthy',
            24: 'Soybean healthy',
            25: 'Squash Powdery mildew',
            26: 'Strawberry Leaf scorch',
            27: 'Strawberry healthy',
            28: 'Tomato Bacterial spot',
            29: 'Tomato Early blight',
            30: 'Tomato Late blight',
            31: 'Tomato Leaf Mold',
            32: 'Tomato Septoria leaf spot',
            33: 'Tomato Spider mites',
            34: 'Tomato Target Spot',
            35: 'Tomato Yellow Leaf Curl Virus',
            36: 'Tomato mosaic virus',
            37: 'Tomato healthy'}


if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(opencv_image,(224,224))
    # Now do something with the image! For example, let's display it:
    st.image(opencv_image, channels="RGB")

    resized = mobilenet_v2_preprocess_input(resized)
    img_reshape = resized[np.newaxis,...]

    Genrate_pred = st.button("Generate Prediction")    
    if Genrate_pred:
        prediction = model.predict(img_reshape).argmax()
        st.title("Predicted Label for the image is")
        st.title("{}".format(map_dict [prediction]))
