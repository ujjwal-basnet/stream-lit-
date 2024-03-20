#load eda pkgs 
import padnas  as pd 
import numpy as np 



#summarization pkgs



# splitter the text into smalle chunks
from langchain.text_splitter import CharacterTextSplitter 

# convert the chunks in document format
from langchain.docstore.document import Document 


from langchain.chains.summarize import load_summarize_chain

#creating prompt 
from langchain import PromptTemplate 

from langchain.llms import CTransformers   # loading the llm model
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import streamlit as st 

#split and convert into documents 
# this function is responsible for splitting the data into smaller chunks and convert the data in document format
def chunks_and_document(txt):
    
    text_splitter = CharacterTextSplitter(chunk_size = 1000 , chunk_overlap = 200 , length_function = len ) # text splitter method by default it has chunk_size = 200 and chunk_overlap = 200
    texts = text_splitter.split_text(txt) # split the text into smaller chunks
    texts = [Document(page_content=t) for t in texts] # convert the splitted chunks into document format
    
    return texts



# Loading the Llama 2's LLM
def load_llm():
    # We instantiate the callback with a streaming stdout handler
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])   

    # loading the LLM model
    # This open source model can be downloaded from here
    # Their are multiple models available just replace it in place of model and try it.
    llm = CTransformers(
        model="/home/ujjwal/ujjwal/stream-lit/nlp-app/llama-2-7b-chat.ggmlv3.q2_K.bin",
        model_type="llama",
         max_new_tokens = 512,
        temperature = 0.5   )
        
    return llm




# this functions is used for applying the llm model with our document 
def chains_and_response(docs):
    
    llm = load_llm()
    chain = load_summarize_chain(llm,chain_type='map_reduce')
    
    return chain.run(docs)





# ecaluate summary 
from rouge  import Rouge
def evaluate_summary(summary , reference):
    r = Rouge()
    eval_score = r.get_scores(summary , reference)
    eval_score_df = pd.DataFrame() 


# Page title

st.set_page_config(page_title='Text Summarization App')
st.title('Text Summarization App')

# Text input
txt_input = st.text_area('Enter your text', '', height=200)

with st.expander(label = "## Your text"  ):
    st.write(txt_input)



result = [] #to store result

# Form to accept user's text input for summarization 
with st.form('summarize_form', clear_on_submit=True):
    submitted = st.form_submit_button('Summarize')
    if submitted:
        with st.spinner('Calculating...'):
            texts = chunks_and_document(txt_input)
            response = chains_and_response(texts)
            result.append(response)




if len(result): # if any text summaries given by model then print the response 
    st.title('📝✅ Summarization Result')
    st.success(response)