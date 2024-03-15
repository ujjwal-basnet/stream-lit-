import streamlit as st 

st.title("Example how to write code")
mycode = """
def hellow():
    print("Hellow my name is Ujjwal Basnet)"""

st.code(mycode , language = 'python' )

