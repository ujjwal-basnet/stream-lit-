#core pkgs 
import streamlit as st 

#load eda pkgs
import pandas as pd 
import numpy as np 

#load data visulization pkgs 



#Matplotlib is used for different usecases like plotting a graph in a script, in a browser or GUIs etc. For each of these cases, 
# matplotlib tries to draw the graph in different ways possible and each of these “ways” is called a backend. 
# It’s all how matplotlib tries to draw and not how we code. The default backend can be changed in many ways including matplotlib.use().

import matplotlib 
matplotlib.use('AGG') #fintype png , raster-graphics : hight quality images using Anti Grain Geomerty Engine 
import matplotlib.pyplot as plt 

def main():
    st.title("plotting with st.pyploy")
    url = 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
    df = pd.read_csv(url)
    st.markdown("First 5 elements ")
    st.dataframe(df.head())
    
    #plotting 
    fig , ax   = plt.subplots() 
    x = np.random.random(150)
    y = np.random.random(150)
    ax.scatter(x  , y )
    st.pyplot(fig)
    
    
    #method -2 
    fig2 = plt.figure()
    df['variety'].value_counts().plot(kind = 'bar')
    st.pyplot(fig2)
    
if __name__ == '__main__':
    main()