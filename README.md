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

### Local Deployment with Docker

1. Build the Docker image
    ```bash
    docker build -t titanic-ml-webapp .
    ```

2. Run the Docker container
    ```bash
    docker run -p 8501:8501 -e PORT=8501 titanic-ml-webapp
    ```

3. Open your browser and go to `http://localhost:8501/`

### Deployment on Heroku

1. Install the Heroku CLI:
    - Follow the instructions [here](https://devcenter.heroku.com/articles/heroku-cli) to install the Heroku CLI.

2. Login to Heroku:
    ```bash
    heroku login
    ```

3. Create a new Heroku application:
    ```bash
    heroku create your-app-name
    ```

4. Set the Heroku stack to container:
    ```bash
    heroku stack:set container -a your-app-name
    ```

5. Set the PORT environment variable:
    ```bash
    heroku config:set PORT=8501 -a your-app-name
    ```

6. Initialize a Git repository (if not already done):
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

7. Add the Heroku remote:
    ```bash
    heroku git:remote -a your-app-name
    ```

8. Deploy to Heroku:
    ```bash
    git push heroku main
    ```

9. Open your Heroku app in the browser:
    ```bash
    heroku open -a your-app-name
    ```

## Technologies Used

- [Python](https://www.python.org/doc/)
- [Flask](https://flask.palletsprojects.com/en/latest/)
- [Streamlit](https://docs.streamlit.io/)
- [Docker](https://docs.docker.com/)
- [Heroku](https://devcenter.heroku.com/categories/reference)
- [Pandas](https://pandas.pydata.org/docs/)
- [Scikit-Learn](https://scikit-learn.org/stable/user_guide.html)
