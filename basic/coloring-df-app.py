import streamlit as st 
import pandas as pd 
from sklearn import datasets 

def main():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data , columns = iris.feature_names)
    
    st.title("Hilight max item")
    st.dataframe(df.iloc[:5 , :-1].style.highlight_max(axis = 0 ))

if __name__ == '__main__':
    main()