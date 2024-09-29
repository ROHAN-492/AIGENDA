import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
genai.configure(api_key="AIzaSyBCua6wbXCM_y41msU9eMOnge37TbAv6vs")
model=genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(input_text, image_data,prompt):
    model.generate_content([input_text,image_data[0],prompt])
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[{"mime_type":uploaded_file.type,"data":bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No file was uploaded")

st.set_page_config(page_title="Rohan's invoice generator")
st.sidebar.header("Robobill")
st.sidebar.write("Made By ROHAN")
st.sidebar.write("By google gemini")
st.header("Robobill")
st.subheader("Made by Rohan")
st.subheader("Manage your expenses")
input=st.text_input("What do you want me to do?:",key="input")
uploaded_file=st.file_uploader("Choose an image",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Upload Image",use_column_width=True)
ssubmit=st.button("Let's Go!")
input_prompt="""You are an expert in understanding invoices. 
We will upload a image as invoices 
and you will have to answer any questions based on the uploaded invoice image
Make sure to greet the user first and then provide the information as suited.
Make sure to keep the font uniform and give the items list in a point-wise format.
At the end, make sure to repeat the name of our app "RoboBill 🦾" and ask the user to use it again.
           
"""

if ssubmit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here's What you need to know!")
    st.write(response)
