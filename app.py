import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os
import PyPDF2
import io

load_dotenv()

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

st.set_page_config(page_title="Resume Analyzer", page_icon="📄")
st.title("📄 Resume Analyzer")
st.markdown("Resume aur Job Description do — main bataunga kya improve karna hai!")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📤 Resume Upload Karo")
    uploaded_file = st.file_uploader("PDF format mein", type=["pdf"])

with col2:
    st.subheader("📋 Job Description")
    job_description = st.text_area("JD yahan paste karo", height=200)

company_name = st.text_input("🏢 Company Ka Naam (optional)")

analyze_btn = st.button("🔍 Analyze Karo!", use_container_width=True)

if analyze_btn:
    if not uploaded_file or not job_description:
        st.error("❌ Resume aur Job Description dono zaroori hain!")
    else:
        with st.spinner("🔍 Analyzing... thoda wait karo..."):

            resume_text = extract_text_from_pdf(uploaded_file)

            prompt = f"""
Tu ek expert Resume Analyzer hai. Neeche resume aur job description diya hai.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

COMPANY NAME: {company_name if company_name else "JD se khud dhundho"}

Ab yeh karo:

1. COMPANY RESEARCH 🏢
   - Company ke baare mein kya jaanta hai
   - Unki culture, values, priorities kya hain
   - Is role mein kaisa banda chahiye

2. RESUME SCORE 📊
   - 100 mein se score do
   - Kyun yeh score diya explain karo

3. STRENGTHS ✅
   - Resume mein kya accha hai
   - JD se kya match kar raha hai

4. WEAKNESSES ❌
   - Kya missing hai resume mein
   - JD mein kya maanga hai jo resume mein nahi

5. IMPROVEMENTS 🚀
   - Exactly kya add karna chahiye
   - Kaise rewrite karna chahiye specific sections
   - Konse keywords add karne chahiye

6. ATS SCORE 🤖
   - ATS systems ke liye kitna optimized hai
   - Kya fix karna chahiye ATS ke liye

Hinglish mein jawab do — simple aur clear.
"""

            client = Groq(api_key=os.getenv("GROQ_API_KEY"))
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )

            st.success("✅ Analysis Complete!")
            st.markdown(response.choices[0].message.content)