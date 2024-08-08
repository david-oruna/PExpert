import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np

from util import set_background


import numpy as np
import joblib
from utils import haller_index_



# Function to test model
def test_model(pectus_tomografía):
    indx = haller_index_(pectus_tomografía)
    model = joblib.load('model.pkl')
    prediction = np.array(model.predict(indx.reshape(-1, 1)))
    prediction_adjusted = np.round(prediction, 2) + 2
    indx_adjusted = np.round(indx, 2) + .5
    recomendaciones = {
        'Normal': 'No se requiere ninguna acción específica. Se recomiendan revisiones periódicas',
        'Leve': 'Considere cambios en el estilo de vida y controle los síntomas. Consultar a un especialista si persisten los síntomas',
        'Moderado': 'Se recomienda consultar a un especialista sobre posibles opciones de tratamiento',
        'Severo': 'Se recomienda consultar inmediatamente a un especialista. Discutir opciones de tratamiento quirúrgico y no quirúrgico.'
    }
    indx_scalar = indx_adjusted.item()
    prediction_scalar = prediction_adjusted.item()
    if indx_scalar < 2.5:
        indxt = 'Normal'
    elif indx_scalar >= 2.5 and indx_scalar < 3.25:
        indxt = 'Leve'
    elif indx_scalar >= 3.25 and indx_scalar < 3.5:
        indxt = 'Moderado'
    else:
        indxt = 'Severo'
    if prediction_scalar < 2.5:
        predictiont = 'Normal'
    elif prediction_scalar >= 2.5 and prediction_scalar < 3.25:
        predictiont = 'Leve'
    elif prediction_scalar >= 3.25 and prediction_scalar < 3.5:
        predictiont = 'Moderado'
    else:
        predictiont = 'Severo'
    return "Diagnóstico: \nÍndice de Haller Actual: {} ({})\n\nÍndice de Haller Post Operatorio: {} ({})\n\nRecomendaciones: {}".format(prediction_scalar, predictiont, indx_scalar, indxt, recomendaciones[predictiont])

# Set background
set_background('PExpert.png')

# Streamlit app
st.title("PExpert")
st.header("Precision and confidence in your pectus surgery")

uploaded_file = st.file_uploader("Please upload your chest CT image in .png or .jpg", type=["png", "jpg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, use_column_width=True)
    diagnosis = test_model(image)
    st.write(diagnosis)