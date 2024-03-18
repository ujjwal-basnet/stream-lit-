#core pkg
import streamlit as st 

#load eda pkgs
import pandas as pd 
import numpy as  np 

def run_eda_app():
    st.subheader("Exploratory Data Analysis")
    url = 'https://raw.githubusercontent.com/lawlesst/vivo-sample-data/master/data/csv/people.csv'
    df = pd.read_csv(url)
    st.markdown("Firt 5 items from dataframe")
    st.dataframe(df.head())
    
    
    st.markdown("shape of the given data frame")
    st.write(df.shape)
    
    
    st.markdown("value counts")
    st.dataframe(df.value_counts())
    
    



    
    