import streamlit as st
import pickle
st.title("Weight Prediction using Height")

height=st.number_input('Enter Height ',min_value=0.0,max_value=70.0,step=0.003)
height=[[height]]

with open('model.pkl','rb') as file:
    model=pickle.load(file)

y_pred=model.predict(height)

if st.button("Predict"):
    st.write(f"Predicted Weight {y_pred}")