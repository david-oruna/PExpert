import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import joblib
import cv2
import base64


def haller_index_(img):
    # Convert the image to a binary image using thresholding

    _, binary_image = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)

    # Define a kernel for morphological operations
    kernel = np.ones((5, 5), np.uint8)

    # Apply morphological opening to remove noise
    opened_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

    # Apply morphological closing to fill gaps
    closed_image = cv2.morphologyEx(opened_image, cv2.MORPH_CLOSE, kernel)
    
    # Find the rows and columns where the binary image is white (255)
    rows, cols = np.where(binary_image == 255)
    min_col, max_col = cols.min(), cols.max()
    center_col = (min_col + max_col) // 2

    # Find the vertical distance between the topmost and bottommost white pixels in the center column
    white_pixel_rows = np.where(binary_image[:, center_col] == 255)[0]
    vertical_distance = white_pixel_rows.max() - white_pixel_rows.min()

    # If the vertical distance is less than 50, use the mean vertical distance
    if vertical_distance < 50:
        vertical_distance = white_pixel_rows.mean()

    # Calculate the horizontal distances for each row
    horizontal_distances = []
    for row in range(binary_image.shape[0]):
        white_pixel_columns = np.where(binary_image[row, :] == 255)[0]
        if white_pixel_columns.size > 0:
            horizontal_distance = white_pixel_columns.max() - white_pixel_columns.min()
            horizontal_distances.append(horizontal_distance)

    # If there are horizontal distances, calculate the Haller index
    if horizontal_distances:
        max_horizontal_distance = max(horizontal_distances)
        haller_index = max_horizontal_distance / vertical_distance
        return haller_index
    else:
        return None
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



def set_background(image_file):
    """
    This function sets the background of a Streamlit app to an image specified by the given image file.

    Parameters:
        image_file (str): The path to the image file to be used as the background.

    Returns:
        None
    """
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
            
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)


if __name__ == "__main__":
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
