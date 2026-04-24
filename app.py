import streamlit as st
from utils.parser import extract_text
from utils.matcher import get_match_score, get_missing_skills

st.title("AI Resume Analyzer")

resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd = st.text_area("Paste Job Description")

if resume and jd:
    resume_text = extract_text(resume)
    score = get_match_score(resume_text, jd)
    missing = get_missing_skills(resume_text, jd)

    st.subheader(f"Match Score: {score}%")
    st.write("Missing Skills:", missing)

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
</style>
""", unsafe_allow_html=True)