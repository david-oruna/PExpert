# PExpert

Python image processing pipeline to support the diagnosis of Pectus Excavatum (PE) and  pipeline allows automatic computation of existing clinical indexes used in PE diagnosis and tratment with unprecedented advantages of avoiding user bias and saving time. Moreover, with the obtained indexes it can predict possible post-surgical indexes outcomes.

# Pectus Project

The Pectus Project aims to develop an innovative tool that improves the evaluation and treatment of Pectus Excavatum by automating the calculation of the Haller index and predicting surgical outcomes.

## Description

Pectus Excavatum (PE) is a congenital deformity of the chest wall that affects both the appearance and functionality of the heart and lungs. The current manual evaluation is slow and prone to errors, and there are no accurate predictive tools for surgical outcomes. The Pectus Project aims to solve these problems by creating an automated system that uses advanced image processing techniques and neural networks.

## Project Structure

### Image Processing Module

- **Description**: Generation of synthetic images due to the lack of real data, allowing the calculation of the Haller index and the creation of a database.
- **Technologies**: Image processing, synthetic data generation.
- **Purpose**: Create realistic and accurate images for model training.

### Outcome Prediction Module

- **Description**: Implementation of a neural network to predict surgical outcomes.
- **Technologies**: TensorFlow, neural networks.
- **Purpose**: Train the model with the synthetic image database and validate its accuracy.

### User Interface

- **Description**: Development of an intuitive interface for doctors.
- **Features**: Allows uploading images, automatically calculates the Haller index, and provides predictions about surgical outcomes.
- **Purpose**: Facilitate decision-making and improve the efficiency of the evaluation process.

## System Requirements

- Python 3.7 or higher
- TensorFlow 2.0 or higher
- Image processing libraries (OpenCV, PIL)
- Framework for the user interface (Tkinter, Flask, etc.)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/user/pectus-project.git
    cd pectus-project
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    pip install -r requirements.txt
    ```

3. Run the user interface:
    ```bash
    python pexpert.py
    ```

## Usage

1. Start the application.
2. Upload a patient's chest image.
3. Automatically calculate the Haller index.
4. Get predictions about surgical outcomes.
5. Use the results to make informed treatment decisions.

## Contributions

Contributions are welcome. Please submit a pull request or open an issue to discuss any changes you would like to make.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or inquiries, please contact David at [d.huamanor@alum.up.edu.pe].

---

Thank you for your interest in the Pectus Project! Together, we can make a significant difference in the lives of those affected by this condition.

## Contributors:
David Huaman
