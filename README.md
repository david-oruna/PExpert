# PExpert

Python image processing pipeline to support the diagnosis of Pectus Excavatum (PE). Allows automatic computation of existing clinical indexes (Haller Index) used in PE diagnosis and treatment with unprecedented advantages of avoiding user bias and saving time. Then with the obtained results from patient pre and post-surgery data, we trained a ML model, making it possible to predict post-surgical indexes.


## Project Structure

![image](https://github.com/user-attachments/assets/b9e3815b-b041-46cb-9391-317d653fc0b2)


### Image Processing Module

- **Description**: Generation of synthetic images due to the lack of real data, allowing the calculation of the Haller index and the creation of a database.

![image](https://github.com/user-attachments/assets/64598858-1556-47f5-acad-ef557e6f7faf)
![image](https://github.com/user-attachments/assets/1bafba1a-1025-457f-bcd1-7525a81dcf5d)


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
- Framework for the user interface (gradio)

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
