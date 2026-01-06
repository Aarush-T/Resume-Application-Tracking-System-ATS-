# Resume Application Tracking System (ATS)

A Gemini-powered ATS that analyzes resumes against job descriptions and provides an ATS-style evaluation.

## Features
- Resume PDF upload
- Job description input
- ATS-style percentage match
- Missing keywords & evaluation
- Secure API key handling

## Tech Stack
- Python
- Streamlit
- Google Gemini (google-genai)
- pdf2image, PIL

## Run Locally
```bash
git clone https://github.com/Aarush-T/Resume-Application-Tracking-System-ATS-.git
cd Resume-Application-Tracking-System-ATS-
conda create -p venv python=3.10 -y
conda activate ./venv
pip install -r requirements.txt
