import streamlit as st
import requests

st.title('Titanic Survival Prediction')

pclass = st.number_input('Pclass', min_value=1, max_value=3, step=1)
sex = st.selectbox('Sex', ['Male', 'Female'])  # 0 for male, 1 for female
age = st.number_input('Age', min_value=0.0)
sibsp = st.number_input('SibSp', min_value=0)
parch = st.number_input('Parch', min_value=0)
fare = st.number_input('Fare', min_value=0.0)

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