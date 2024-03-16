import streamlit as st 
import pandas as pd 


#select / multiple select 
my_lang = ['python' , 'java' , 'c++']
Multiple_select = st.checkbox(label = "Multiple select" , value  = False )


#single select (select box)

single_select = st.checkbox(label = "Select-Box" , value = False   )

#slider 
slider = st.checkbox(label = "Slider" , value = False )





if Multiple_select == True :
    st.title("Multiple_select")
    options = st.multiselect(label = 'Language' , options= my_lang , default= 'java')
    st.write('You chose' , options )
    
    
    
if single_select == True :
    st.title("single_select")
    options = st.selectbox(label='Language' , options = my_lang  )
    st.write("you choose" , options )
    

if slider  == True :
    st.title("slider")
    option = st.slider(label = "Age" , min_value= 5 , max_value= 100)
    st.write("Your age is " , option)

