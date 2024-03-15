#here we will see all about magic function of st-write-py

import streamlit as st 
from sklearn import datasets
import pandas as pd 

def main():
    st.write("# This is header ")
    st.write("##  THis is H2 header")
    st.write("### This is H3 header")
    
    # you can also do maths like
    st.write("16 * 6 is {}".format(16*6))
    
    #create a tittle 
    st.text("This is text from st.text")
    st.write("This text from st.title ")
    st.title("Title from st.title")
    st.title("Help info ")
    #display helpful docs abt print
    st.help(print)

    st.title("also")
    st.write(dir(print))
    
    #display dataframe 
    cancer_ = datasets.load_breast_cancer()
    df_cancer = pd.DataFrame(cancer_.data , columns =cancer_.feature_names)
    st.write(df_cancer.head())
if __name__ =='__main__':
    main()