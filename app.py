import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader  # Use pypdf instead of PyPDF2

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def get_gemini_response(input_text, pdf_text, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_text, pdf_text, prompt])
    return response.text

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    pdf_text = "\n".join(page.extract_text() or "" for page in reader.pages)
    return pdf_text.strip() if pdf_text.strip() else "No extractable text found in the PDF."

# Streamlit App
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")
    pdf_text = extract_text_from_pdf(uploaded_file)
else:
    pdf_text = None

submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage match")

input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First, the output should come as a percentage, followed by missing keywords, and finally, final thoughts.
"""

if submit1 and pdf_text:
    response = get_gemini_response(input_text, pdf_text, input_prompt1)
    st.subheader("The Response is:")
    st.write(response)
elif submit3 and pdf_text:
    response = get_gemini_response(input_text, pdf_text, input_prompt3)
    st.subheader("The Response is:")
    st.write(response)
else:
    if (submit1 or submit3) and not uploaded_file:
        st.write("Please upload the resume")
