#core pkgs 
import streamlit as st 

# This must be the first Streamlit command used on an app page,
st.set_page_config(page_title = 'Ujjwal APP' ,
                   page_icon = ':smiley:' , 
                   layout= 'centered' , 
                   initial_sidebar_state = 'collapsed' 
)


# and must only be set once per page.st.set_page_config()

#discription 
print(""" 
      
      function 
      st.set_page_config(page_title=None, page_icon=None,
                layout="centered", 
                initial_sidebar_state="auto",
                menu_items=None)
      
      
      """ )
def main() :
    st.title("hellow hellow ")
    st.write("watch on top")
    st.sidebar.success("Menu")
    

if __name__ == '__main__':
    main()