# 📄 Resume Analyzer AI

> An intelligent resume analysis tool powered by LLaMA 3.3 that evaluates your resume against job descriptions and provides actionable feedback to maximize your chances of landing the job.

---

## 🌟 Features

- **📤 Resume Upload** — Upload your resume in PDF format
- **📋 JD Analysis** — Paste any job description for comparison
- **🏢 Company Research** — Get insights about the company culture and expectations
- **📊 Resume Score** — Get a score out of 100 with detailed reasoning
- **✅ Strengths** — Know what's working in your resume
- **❌ Weaknesses** — Identify gaps between your resume and the JD
- **🚀 Improvements** — Get specific suggestions to rewrite and strengthen your resume
- **🤖 ATS Optimization** — Check how well your resume performs against ATS systems

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web UI framework |
| Groq API (LLaMA 3.3) | AI analysis engine |
| PyPDF2 | PDF text extraction |
| python-dotenv | Secure API key management |

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10 or above
- Groq API Key — Get it free at [console.groq.com](https://console.groq.com)

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/Yuvraj-arch79/resume-analyzer.git
cd resume-analyzer
```

**2. Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create `.env` file**
```bash
GROQ_API_KEY=your_groq_api_key_here
```

**5. Run the app**
```bash
streamlit run app.py
```

**6. Open in browser**
```
http://localhost:8501
```

---

## 📖 How To Use

1. Upload your resume as a PDF file
2. Paste the job description of the role you are applying for
3. Optionally enter the company name for deeper research
4. Click **Analyze** and get detailed feedback in seconds

---

## 📁 Project Structure

```
resume-analyzer/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # API keys (not pushed to GitHub)
├── .gitignore             # Files to ignore in Git
└── README.md              # Project documentation
```

---

## 🔒 Security

- API keys are stored in `.env` file
- `.env` is added to `.gitignore` — never pushed to GitHub
- No user data is stored or logged

---

## 🚀 Deployment

This app can be deployed for free on **Streamlit Cloud**:

1. Push your code to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Add `GROQ_API_KEY` in the secrets section
5. Deploy with one click
