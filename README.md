
# 🤖 AI ICP Fit Evaluator

## 📘 Project Overview
The **AI ICP Fit Evaluator** is an intelligent Streamlit-based tool that automatically evaluates whether a candidate’s profile fits an **Ideal Customer Profile (ICP)** or **Ideal Candidate Profile** for a given **Job Description (JD)**.  

It leverages **Google Gemini AI** to analyze resumes, LinkedIn profile text, or “About” sections and provides a quick and concise decision — **Fit** or **Not Fit** — along with a short reasoning (2–3 sentences).  

This application helps HR teams, recruiters, and business leaders assess candidates efficiently without manually reviewing long resumes or profiles.

---

## ⚙️ How It Works

1. **Input Candidate Information**
   - 📄 Upload Resume (TXT or PDF)  
   - 📝 Paste LinkedIn “About” or Profile Text  
   - 🔗 Provide LinkedIn Profile URL (*currently disabled — no public LinkedIn API available*)

2. **Provide Job Description**
   - Paste JD text directly, or  
   - Upload a JD file (TXT or PDF).

3. **Load ICP Rules**
   - The app reads rules from `icp_rules.json` containing:
     - 🎯 Target roles  
     - 🧠 Required skills  
     - 💼 Target industries  
     - ⏱️ Minimum experience years  

4. **AI Evaluation (Google Gemini)**
   - The system sends all details (JD + Candidate Data + ICP Rules) to Google Gemini AI.
   - Gemini analyzes and returns:
     ```
     Fit Status: Fit / Not Fit
     Reason: (2–3 sentences)
     ```

5. **Display Result**
   - The result is shown on the page with a clean, modern UI.

---

## 🚫 LinkedIn Profile URL Notice
Currently, **LinkedIn profile URLs cannot be read automatically**, as LinkedIn has discontinued public APIs and third-party data scrapers (Proxycurl, RapidAPI, etc.).  

👉 **Alternative:**  
You can either:
- **Upload a candidate resume (TXT or PDF)**, or  
- **Paste their LinkedIn "About" text** manually into the text box.

---

## 💡 Example Use Case

**Job Description:**
> .NET Developer with experience in C#, ASP.NET Core, Web APIs, and Azure DevOps.

**Candidate Resume:**
> 5 years of experience building REST APIs using .NET Core, C#, and SQL Server.  
> Worked on Azure pipelines for CI/CD and deployed applications in production.

**AI Output:**
```
Fit Status: ✅ Fit
Reason: The candidate has solid .NET Core and Azure experience matching the JD requirements.
```

---

## 🧠 Key Features
✅ Instant AI-based profile evaluation  
✅ Resume and LinkedIn text input options  
✅ Configurable ICP rule engine (`icp_rules.json`)  
✅ Professionally designed Streamlit UI  
✅ Secure API key storage via `.env`  
✅ Fully responsive and deployable on Render  

---

## 🧰 Technologies Used

| Category | Tools / Frameworks |
|-----------|--------------------|
| 💻 **Frontend** | Streamlit, HTML, CSS |
| 🤖 **AI Engine** | Google Gemini AI API |
| 🧠 **Backend / Logic** | Python 3.10+ |
| 📦 **Dependencies** | PyPDF2, python-dotenv, google-generativeai, requests |
| ☁️ **Deployment** | Render (Cloud Hosting for Streamlit Apps) |
| ⚙️ **Configuration** | `.env` for keys, `icp_rules.json` for rules |

---

## 🧩 Project Structure
```
📂 ai_icp_fit_evaluator/
│
├── app.py                # Main Streamlit app
├── icp_rules.json        # Configurable ICP rules
├── .env                  # API keys and environment variables
├── logo.png              # Company logo displayed in header (base64 encoded)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🔑 Environment Setup

Create a `.env` file in your project folder with your Google Gemini API key:
```bash
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

---

## 🚀 Run the Application

### 1️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 2️⃣ Run Streamlit app:
```bash
streamlit run app.py
```

Then open the provided local URL (usually `http://localhost:8501`).

---

## 🧾 Example ICP Rules (`icp_rules.json`)

```json
{
  "target_industries": ["Technology", "Finance", "Healthcare"],
  "target_roles": ["Data Analyst", "SQL Developer", "Power BI Developer", "Data Engineer"],
  "required_skills": ["SQL", "Power BI", "Python", "ETL"],
  "minimum_experience_years": 2
}
```

**You can customize this file** for each type of evaluation, for example:

```json
{
  "target_industries": ["IT Services", "Software Development"],
  "target_roles": [".NET Developer", "Software Engineer", "Backend Developer"],
  "required_skills": ["C#", ".NET Core", "ASP.NET", "Web API", "SQL Server", "Azure DevOps"],
  "minimum_experience_years": 3
}
```

---

## 🎨 UI Highlights
- Modern gradient title bar with embedded logo (Base64)
- Center-aligned AI title and tagline
- Clean section-based layout (cards)
- Large, responsive “Evaluate Fit” button
- Full-screen output card with AI-generated results

---

## 🧾 Future Enhancements
- 🔗 Re-enable LinkedIn API integration when available  
- 🧮 Add candidate scoring (0–100 scale)  
- 📊 Export evaluation reports as JSON or Excel  
- 🧩 Enable multi-candidate batch evaluations  
- ⚙️ Add ICP rule editing directly within the UI  

---

## ✨ Summary
The **AI ICP Fit Evaluator** automates candidate-job fit evaluation using the power of **Google Gemini AI**, **Python**, and **Streamlit**.  
By supporting resume uploads, LinkedIn text, and configurable ICP criteria, it delivers structured, fast, and visually engaging results for talent assessment.

---

## 💙 Credits
**Developed & Designed by:** *Taviti Naidu Reddy*  
**Powered by:** [Google Gemini AI](https://aistudio.google.com) • [Streamlit](https://streamlit.io) • [Python](https://www.python.org)  
🚀 *Built with passion and precision!*
