import streamlit as st 


def main() :
    st.title("Summrizer APP")
    menu  = [ "Home" , "About"]
    choice = st.sidebar.selectbox(label= "Menu" , options= menu)
    
    if choice  =='Home':
        st.subheader("Summrization")
        raw_text = st.text_area("Your text here ")
        if st.button("Summarize"):
            st.write(raw_text)
        
        
    else :
        st.subheader("About")
        st.markdown("NLP SUmmarizer App")
    
    
    
    


if __name__ =='__main__':
    main()