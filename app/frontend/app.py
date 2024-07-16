import streamlit as st
import requests

st.set_page_config(page_title="Titanic Survival")

st.title('Titanic Survival Prediction')

pclass = st.number_input('Class', min_value=1, max_value=3, step=1)
sex = st.selectbox('Sex', ['Male', 'Female'])  # 0 for male, 1 for female
age = st.number_input('Age', min_value=0.0)
sibsp = st.number_input('Number of siblings and spouses travelling with the passenger', min_value=0)
parch = st.number_input('Number of children travelling with the passenger', min_value=0)
fare = st.number_input('Ticket Fare', min_value=0.0)

if sex == 'Male':
    sex = 0
else:
    sex = 1

if st.button('Predict'):
    data = {
        'data': [pclass, sex, age, sibsp, parch, fare]
    }
    response = requests.post('http://127.0.0.1:5000/predict', json=data)
    prediction = response.json()['prediction']
    result = 'Survived' if prediction == 1 else 'Did not survive'
    st.write(f'Prediction: {result}')