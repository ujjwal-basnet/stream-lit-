import streamlit as st
import pickle
import numpy as np

# Load pickled model
model = pickle.load(open('car-prediction-streamlit/random-forest-ujjwal.pkl', 'rb'))

# Predict value given by the user
def pred_price(Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner, no_year):
    # Convert input data to appropriate data types
    Present_Price = float(Present_Price)
    Kms_Driven = float(Kms_Driven)
    Owner = int(Owner)
    no_year = float(no_year)

    # Convert categorical features to numerical values
    fuel_type_mapping = {'CNG': 0, 'Disel': 1, 'Petrol': 2}
    seller_type_mapping = {'Dealer': 0, 'Petrol': 1}
    transmission_mapping = {'Atuomatic': 0, 'Manual': 1}

    Fuel_Type = fuel_type_mapping[Fuel_Type]
    Seller_Type = seller_type_mapping[Seller_Type]
    Transmission = transmission_mapping[Transmission]

    out_input = np.array([[Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner, no_year]]).astype(np.float64)

    # Make prediction
    prediction = model.predict(out_input)

    return float(prediction)

st.title("Car Price Prediction")
st.success("#### Used Car Prediction ML APP")

Present_Price = st.text_input(label="What is the Current Market Value Of the car", value="IN LACKS")
Kms_Driven = st.text_input(label='How much kilogram does the car has driven?', value='0')
Fuel_Type = st.selectbox(label="Fuel type", options=['CNG', 'Disel', 'Petrol'])
Seller_Type = st.selectbox(label="Type of seller", options=['Dealer', 'Petrol'])
Transmission = st.selectbox(label="Type of Transmission", options=['Atuomatic', 'Manual'])
Owner = st.selectbox(label="No of owners", options=[1, 2, 3])
no_year = st.text_input(label='How Many Years old', value='0')

# Submit
if st.button(label="Predict"):
    output = pred_price(Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner, no_year)
    st.success('The selling price of this vehicle will be approximately {} lakhs'.format(round(output, 2)))