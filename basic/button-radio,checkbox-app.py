import streamlit as st 

st.button("This is button")
st.checkbox("This is checkbox")

#implementation 
name  = "ujjwal"
if st.button("click to know my name "):
    st.write("Name : {}".format(name))

#you cannot use same name for two button thus we need key to defines
#below code through error's
#if st.button("click to know my name") 


if st.button("click to know my name" , key = 'new'):
    st.write('name : {}'.format(name))


if st.button("Click to know my name "  , key = 'new1'):
    st.write("ujjwal")
st.title("Working with radio button ")

st.write("verticle")
st.radio(label= "# Gender", options= ['male' , 'female'] , captions= ['select here if you are male ' , 'select here if you are gay'] , horizontal= False )

st.write("Horizontal")
st.radio(label= "# Gender", options= ['male' , 'female'] , captions= ['select here if you are male ' , 'select here if you are gay'] , horizontal= True )


st.title("Another example ")
status = st.radio(label = 'what is your status '  , options = ['Active' , 'In-Active'])
if status == 'Active':
    st.success("Your are  Active🔥 ")
else :
    st.warning("You are inactive 🤖 ")

st.title("Check-Box")
male = st.checkbox(label = "Male" , value = False)
print(male)
if male == True:
    st.write("You select Male")
female = st.checkbox(label = "Female" , value = False )

if female == True:
    st.write("You select Female")
    
st.title("expender")

with st.expander("Ujjwal"):
    st.text("He is a great guy")
    
st.bar_chart({'data' : [1 , 2 , 4 ,5 ]})
with st.expander("Know more"):
    st.write("This is a bar cart created using streamlit code ")
    st.code("st.bar_cart({'data' : [1 , 2 ,4 ,5]})" , language= 'python')