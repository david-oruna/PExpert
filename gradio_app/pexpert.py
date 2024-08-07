import numpy as np
import joblib
import gradio as gr

def test_model(pectus_tomografía):
    indx = haller_index_(pectus_tomografía)
    model = joblib.load('model.pkl')
    # Ensure prediction is a numpy array
    prediction = np.array(model.predict(indx.reshape(-1, 1)))
    
    # Perform the addition
    prediction_adjusted = np.round(prediction, 2) + 2
    
    # Ensure indx is processed similarly
    indx_adjusted = np.round(indx, 2) + .5
    recomendaciones = {
        'Normal': 'No se requiere ninguna acción específica. Se recomiendan revisiones periódicas',
        'Leve': 'Considere cambios en el estilo de vida y controle los síntomas. Consultar a un especialista si persisten los síntomas',
        'Moderado': 'Se recomienda consultar a un especialista sobre posibles opciones de tratamiento',
        'Severo': 'Se recomienda consultar inmediatamente a un especialista. Discutir opciones de tratamiento quirúrgico y no quirúrgico.'
    }

    # Adjusted to handle scalar value from numpy array
    indx_scalar = indx_adjusted.item()  # Convert numpy array to scalar
    prediction_scalar = prediction_adjusted.item()  # Convert numpy array to scalar

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

iface = gr.Interface(fn=test_model, inputs="image", outputs="text")
iface.launch(share=True)