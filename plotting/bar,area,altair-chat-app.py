#core pkgs
import streamlit as st 

#load eda pkgs
import numpy as np 
import pandas as pd 

def main():
    st.title("Plotting in Streamlit ")
    
    #Load Dataset
    st.title("plotting with st.pyploy")
    url = 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
    df_iris = pd.read_csv(url)
    st.markdown("First 5 elements ")
    st.dataframe(df_iris.head())
    
    
    

    
   #streamlit_area_Chart 
    st.title("Area_chart")
    st.code(""" st.area_chart(data=None, *, 
            x=None, y=None, color=None, width=0,
            height=0, use_container_width=True)""")
    
    df = pd.DataFrame(np.random.randn(20 , 3 )  , columns = ["a" , "b" , "c"] )
    st.dataframe(df.head())
    st.area_chart(df)

    
    
    st.header('Bar chart')
    st.code(""" st.bar_chart(data=None, *, x=None,
            y=None, color=None, width=0, 
            height=0,
            use_container_width=True)""")
    
    st.bar_chart(data = df_iris , x  = 'variety')
    st.bar_chart(df)
    
    st.header("st.line_chart")
    st.code("""
             st.line_chart(data=None, *,
             x=None, y=None, color=None, 
             width=0, height=0, 
             use_container_width=True)
            """)
    
    st.line_chart(data = df )
    choice = st.multiselect(label = "select line chart" , options = list(df_iris.columns))
    st.line_chart(df_iris[choice])
    
    st.area_chart(df_iris[choice] , use_container_width= True)
    
    #work with atiar 
    
    
    
if __name__ =='__main__':
    main()
   
