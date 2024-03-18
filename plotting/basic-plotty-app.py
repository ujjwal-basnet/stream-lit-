import streamlit as st 

#load eda pkg 
import pandas as pd 
import numpy as np 

#load Data visulization pkg 
import plotly.express as px 
#The plotly.express module (usually imported as px) 
# contains functions that can create entire figures at on

def main():
    st.title("Plotting IN Streamlit With Plotly")
    df = pd.read_csv('media/pro-lang.xls')
    st.dataframe(df)
    fig = px.pie(df , values ='count' , names = 'name', title= 'Pie Charts')
    st.plotly_chart(fig)
    
    
    fig2 = px.bar(df , x  = 'name' , y = 'name')
    st.plotly_chart(fig2)

if __name__ == '__main__':
    main()