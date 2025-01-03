import pandas as pd
import numpy as np
import streamlit as st
import pickle

with open("model.pkl","rb") as f:
    load_model = pickle.load(f)

model = load_model['model']
feature_names = load_model['feature_names']

st.title("Rainfall Prediction")
st.write("Fill in the details below to predict rainfall:")

def user_input():
    inputs = {}
    inputs['pressure'] = st.number_input("Pressure", min_value=998.0, value = 1000.0)
    inputs['dewpoint'] = st.number_input("Dewpoint", min_value=-0.5, value = 0.0)
    inputs['humidity'] = st.number_input("Humidity", min_value=0.0, value = 30.0)
    inputs['cloud'] = st.number_input("Cloud", min_value=0.0, value = 20.0)
    inputs['sunshine'] = st.number_input("Sunshine", min_value=0.0, value = 4.0)
    inputs['winddirection'] = st.number_input("Winddirection", min_value=0.0, value = 200.0)
    inputs['windspeed'] = st.number_input("Windspeed", min_value=2.0, value = 20.0)
    return inputs

user_inputs = user_input()
input_data = pd.DataFrame([user_inputs],columns=feature_names)

if st.button("Predict Rain"):
    prediction = model.predict(input_data)
    result = "Rainfall" if prediction[0] == 1 else "No Rainfall"
    st.subheader(f"Prediction: {result}")