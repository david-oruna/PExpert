import streamlit as st
from PIL import Image
import numpy as np
from util import set_background
from utils import haller_index_
import joblib


# Function to test model
def test_model(pectus_tomografía):
    indx = haller_index_(pectus_tomografía)
    model = joblib.load('model.pkl')
    prediction = np.array(model.predict(indx.reshape(-1, 1)))
    prediction_adjusted = np.round(prediction, 2) + 2
    indx_adjusted = np.round(indx, 2) + .5
    recomendaciones = {
      'Normal': 'No specific action required. Periodic check-ups are recommended',
        'Mild': 'Consider lifestyle changes and manage symptoms. Consult a specialist if symptoms persist',
        'Moderate': 'Consult a specialist about possible treatment options',
        'Severe': 'Immediate consultation with a specialist is recommended. Discuss surgical and non-surgical treatment options.'
    }
    indx_scalar = indx_adjusted.item()
    prediction_scalar = prediction_adjusted.item()
    if indx_scalar < 2.5:
        indxt = 'Normal'
    elif indx_scalar >= 2.5 and indx_scalar < 3.25:
        indxt = 'Mild'
    elif indx_scalar >= 3.25 and indx_scalar < 3.5:
        indxt = 'Moderate'
    else:
        indxt = 'Severe'
    if prediction_scalar < 2.5:
        predictiont = 'Normal'
    elif prediction_scalar >= 2.5 and prediction_scalar < 3.25:
        predictiont = 'Mild'
    elif prediction_scalar >= 3.25 and prediction_scalar < 3.5:
        predictiont = 'Moderate'
    else:
        predictiont = 'Severe'
    return "Diagnóstico: \nÍndice de Haller Actual: {} ({})\n\nÍndice de Haller Post Operatorio: {} ({})\n\nRecomendaciones: {}".format(prediction_scalar, predictiont, indx_scalar, indxt, recomendaciones[predictiont])

# Set background
set_background('deploy/PExpert.png')

# Streamlit app
st.title("PExpert")

st.markdown(body="Calculates *haller index* and predicts possible **post surgery results**", unsafe_allow_html=False, help=None)
sidebar_logo = "deploy/PEXPERT__1_-removebg-preview.png"
main_body_logo ="deploy/PEXPERT__2_-removebg-preview.png"
st.logo(sidebar_logo, icon_image=main_body_logo)
st.sidebar.markdown("Steps: \n\n1. Upload your chest CT image in .png or .jpg format. \n\n2. Click on the 'Predict' button to get the results.")

uploaded_file = st.file_uploader("Please upload your chest CT image in .png or .jpg", type=["png", "jpg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('L')
    st.image(uploaded_file, use_column_width=True, caption="Your uploaded image")
    st.write("Calculating Haller index and predicting post surgery results...")
    indx = haller_index_(np.array(image))
    if indx is not None:
        st.write(test_model(np.array(image)))
    else:
        st.write("No Haller index calculated. Please upload a different image.")
    
