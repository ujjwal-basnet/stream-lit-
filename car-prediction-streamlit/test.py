import streamlit as st 
Fuel_Type = st.selectbox(label = "Fuel type" , options  = ['CNG' , 'Disel' , 'Petrol'])
st.write('you choose ' , Fuel_Type)
st.write(type(Fuel_Type))
print(Fuel_Type)