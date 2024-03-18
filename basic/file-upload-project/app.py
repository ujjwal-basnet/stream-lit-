#core pkg 
import streamlit as st 

#image processing pkg 
from PIL import Image 

#data processing  pkg
import numpy as np 
import pandas as pd 


#to work with pdf 
from PyPDF2 import PdfReader 

#setup 
st.set_page_config(page_title = "App" , page_icon = ":sparkles" , initial_sidebar_state= "collapsed")



# pkg to convert docs file to text file 
import docx2txt

#load image
@st.cache_resource
def load_img(img_loc):
    img = Image.open(img_loc)
    return  img

#read pdf 
def read_pdf(file):
    pdf_reader = PdfReader(file)
    text = ''
    for i in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[i] 
        text = page.extract_text() + text 
        
    return text



def read_docs(file):
    txt  = docx2txt.process(file)
    return txt

def main():
    st.title("File Upload Tutorial")
    choose = ['Home' , 'Documents' , 'Csv'] 
    choice = st.sidebar.selectbox(label = "Menu" , options= choose) 
    
    
#home 
    if choice =='Home':
        st.subheader("Home")
        image_file = st.file_uploader(label = "Upload Images" , 
                                      type = ['png' , 'jpg' , 'jpeg'])
        if image_file is not None :
            #see details of the image 
            img_details = {"file_name" : image_file.name , 
                           'file_type': image_file.type , 
                           'size' : image_file.size 
                            }
            st.write(img_details)
            st.image(load_img(image_file) , width = 550  , caption = image_file.name)
            
            
            
            
#csv    
    elif choice == 'Csv':
        st.subheader("CSV")
        csv_file = st.file_uploader(label= "Upload csv" ,
                                     type = ['csv'])
        if csv_file is not None :
            csv_details = {"file-name" : csv_file.name , 
                           "file-type" : csv_file.type , 
                           "size" : csv_file.size}
            st.write(csv_details)
            df = pd.read_csv(csv_file)
            st.dataframe(df)
            
            
#Documents

    elif choice =='Documents':
        st.subheader("Documents") 
        doc_file = st.file_uploader("Upload Documents" ,
                                      type = ['pdf' , 'docx' ,'txt'])            
        if st.button(label= 'Process') :
            if  doc_file is not None :
                doc_details = {'file_name'  : doc_file.name , 
                               'file_type' : doc_file.type , 
                               'file_size' : doc_file.size}
                st.write(doc_details)
                if doc_file.type =='text/plain':
                    #read 
                    raw_text = str(doc_file.read() , 'utf-8')
                    #st.write(raw_text)
                    st.text(raw_text) #st.text works better
                    
                    
                    
                    
                    
                elif doc_file.type == 'application/pdf':
                    content = read_pdf(doc_file)
                    st.text(content)                   
                
                else :
                    content = read_docs(doc_file)
                    st.write(content)
    
    
if __name__ =='__main__':
    main()