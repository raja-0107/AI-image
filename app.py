import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

myrobo= genai.Client(api_key="AIzaSyCqF-F8bfJMvIxj8DUcjJM1HVr-NMh6JJE")
col1,col2=st.columns(2)
with col1:
    st.title("IMAGE CREATOR")
    userdata=st.text_area(" ")
    if st.button("SEND"):
        answer=myrobo.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=userdata,
            config=types.GenerateContentConfig(
            response_modalities=['TEXT','IMAGE']
            )
        )
        for part in answer.candidates[0].content.parts:
            if part.text is not None:
                print(part.text)
            elif part.inline_data is not None:
                image=Image.open(BytesIO((part.inline_data.data)))
                image.save("Myimage.png")

with col2:
    if st.image("Myimage.png"):
        st.write("Your Image Has Been Created Successfully")

    else:
        st.write("Waiting for Your Response......")
       
             
