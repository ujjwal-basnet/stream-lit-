import streamlit as st 
import pandas as pd 
from sklearn import datasets 



def main() :
#load datasets
    iris_ = datasets.load_iris()
    df = pd.DataFrame(iris_.data,columns=iris_.feature_names)
    st.dataframe(df) #or st.write(df)
    
    st.header("Printing only head (5 values)")
    st.dataframe(df.head()) # or st.write(df.head())
    
    st.header("print from last" )
    st.dataframe(df.tail()) # or st.write(df.tail())
    
    st.dataframe(df.iloc[:5 , :-1])
if __name__ == '__main__':
 main()
    
    

