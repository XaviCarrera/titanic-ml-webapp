# Titanic ML Web App

This is a simple web application that predicts Titanic survival using a Machine Learning model.

## Installation

1. Clone the repository
    ```bash
    git clone https://github.com/XaviCarrera/titanic-ml-webapp.git
    cd titanic-ml-webapp
    ```

2. Create a virtual environment and install dependencies
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Train the model
    ```bash
    python3 model_training/train_model.py
    ```

4. Run the application
    ```bash
    python3 app/app.py
    streamlit run app/frontend/app.py
    ```

5. Open your browser and go to `http://127.0.0.1:8501/`

## Usage

Fill in the form with the required details and submit to get the prediction.

## Deployment

Follow the specific guidelines of your chosen platform to deploy this application.
