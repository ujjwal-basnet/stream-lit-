#core pkg
import streamlit as st 

#import our mini apps 
from eda_app import run_eda_app 
from ml_app import run_ml_app


def main() :
    st.title("Main App") 
    menu = ['Home' , 'EDA' , 'ML' , 'About']
    choice = st.sidebar.selectbox(label = "Menu" , options = menu)
    
    #condition
    if choice == 'Home':
        st.subheader('Home')
    
    
    elif choice == 'EDA':
        st.subheader('EDA')
        run_eda_app()
        
    
    
    
    elif choice == 'ML':
        st.subheader("ML")
        run_ml_app()
    else :
        st.subheader("About")
        
        


if __name__ == '__main__':
    main()