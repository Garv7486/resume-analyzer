# AI Resume Analyzer

## Overview
AI Resume Analyzer is a machine learning-based web application that analyzes a candidate’s resume and compares it with a job description. It calculates a match score and highlights missing skills to help improve job readiness.

## Features
- Resume parsing (PDF support)
- Job description matching
- Match score calculation using NLP (TF-IDF + Cosine Similarity)
- Missing skills identification
- Simple and interactive web interface

## Tech Stack
- Python
- Streamlit
- Scikit-learn
- PyMuPDF
- Matplotlib

## Project Structure
resume-analyzer/
│── app.py
│── requirements.txt
│── README.md
│── images/
│ └── demo.png
└── utils/
├── parser.py
├── preprocess.py
└── matcher.py


## How It Works
1. Upload a resume in PDF format.
2. Enter a job description.
3. The system extracts text from the resume.
4. It compares the resume with the job description using NLP techniques.
5. A match score and missing skills are displayed.

## Installation and Setup

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/resume-analyzer.git
cd resume-analyzer

2. Create virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run the application
streamlit run app.py

<img width="1920" height="1012" alt="Screenshot" src="https://github.com/user-attachments/assets/b913e446-96e8-43eb-a4a8-53c5a1c3d053" />

License

This project is open source and available under the MIT License.
