from dotenv import load_dotenv
load_dotenv()
from google.genai import types

import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
from google.genai import Client

# ---------------- Gemini Client ----------------

client = Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_gemini_response(input, pdf_content, prompt):
    response = client.models.generate_content(
        model="models/gemini-1.5-flash",  # ✅ FIXED
        contents=[
            input,
            pdf_content,
            prompt
        ]
    )
    return response.text


# ---------------- PDF Processing ----------------

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format="JPEG")

        return types.Part.from_bytes(
            data=img_byte_arr.getvalue(),
            mime_type="image/jpeg"
        )
    else:
        raise FileNotFoundError("No file uploaded")


# ---------------- Streamlit UI ----------------

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader(
    "Upload your resume (PDF)...",
    type=["pdf"]
)

if uploaded_file is not None:
    st.success("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage Match")

input_prompt1 = """
You are an experienced Technical Human Resource Manager.
Review the provided resume against the job description.
Highlight strengths and weaknesses related to the role.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System).
Evaluate the resume against the job description.
Return:
1) Percentage match
2) Missing keywords
3) Final thoughts
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(
            input_prompt1,
            pdf_content,
            input_text
        )
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(
            input_prompt3,
            pdf_content,
            input_text
        )
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please upload the resume")

        
#cd C:\Users\User\OneDrive\Desktop\ATS
#conda activate .\venv
#streamlit run app.py
