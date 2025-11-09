import streamlit as st
import google.generativeai as genai
import os
import json
import base64
from dotenv import load_dotenv
from PyPDF2 import PdfReader

# ==============================
# ENV SETUP
# ==============================
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ==============================
# VALIDATE GOOGLE GEMINI API KEY
# ==============================
def validate_google_api_key(api_key):
    if not api_key:
        return False
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")
        model.generate_content("ping")
        return True
    except Exception:
        return False


if not validate_google_api_key(GOOGLE_API_KEY):
    st.set_page_config(page_title="AI ICP Fit Evaluator", page_icon="🤖", layout="wide")
    st.title("❌ Invalid Google API Key")
    st.error("""
    Your Google Gemini API key is invalid or missing.

    👉 Fix:
    1. Visit [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
    2. Create a new API key.
    3. Add it to your `.env` file:
       ```
       GOOGLE_API_KEY=your_new_key_here
       ```
    4. Save and restart the app.
    """)
    st.stop()

# ==============================
# LOAD ICP RULES
# ==============================
def load_icp_rules():
    try:
        with open("icp_rules.json", "r") as f:
            return json.load(f)
    except Exception as e:
        st.warning(f"⚠️ Could not load rules file: {e}")
        return {}

rules = load_icp_rules()

# ==============================
# FILE READER
# ==============================
def read_file(uploaded_file):
    text = ""
    if uploaded_file:
        if uploaded_file.name.endswith(".txt"):
            text = uploaded_file.read().decode("utf-8", errors="ignore")
        elif uploaded_file.name.endswith(".pdf"):
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    return text.strip()

# ==============================
# LOAD COMPANY LOGO AS BASE64
# ==============================
def load_logo_base64(logo_path):
    """Convert local logo image to base64 string for inline HTML."""
    if not os.path.exists(logo_path):
        return ""
    with open(logo_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")

logo_path = "company_logo.png"  # 👈 replace with your own logo filename
logo_base64 = load_logo_base64(logo_path)

# ==============================
# CUSTOM STYLES
# ==============================
st.set_page_config(page_title="AI ICP Fit Evaluator", page_icon="🤖", layout="wide")

st.markdown(
    """
    <style>
        body {
            background: linear-gradient(120deg, #f5f7fa, #e8f0fe);
        }
        .main {
            padding: 0rem 3rem;
        }
        .title-bar {
            background: linear-gradient(to right, #1565c0, #42a5f5);
            color: white;
            padding: 20px 40px;
            border-radius: 16px;
            box-shadow: 0px 5px 15px rgba(0,0,0,0.15);
            margin-bottom: 35px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .title-center {
            flex: 1;
            text-align: center;
        }
        .title-center h1 {
            font-size: 2.4em;
            font-weight: 800;
            margin-bottom: 5px;
        }
        .title-center p {
            margin-top: 0;
            font-size: 1em;
        }
        .title-logo {
            width: 200px;           /* increased from 70px */
            height: 120px;          /* increased from 70px */
            border-radius: 16px;
            object-fit: contain;
            background: white;
            padding: 10px;          /* a bit more padding for clean edges */
            box-shadow: 0px 4px 10px rgba(0,0,0,0.25);
        }

        .section-card {
            background-color: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            margin-bottom: 25px;
        }
        .output-card {
            background-color: white;
            border-radius: 15px;
            padding: 45px;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
            margin-top: 25px;
        }
        .stButton>button {
            background: linear-gradient(to right, #1976d2, #42a5f5);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 18px 30px;
            font-size: 18px;
            font-weight: 600;
            width: 100%;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(to right, #0d47a1, #1e88e5);
            transform: scale(1.02);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# TITLE BAR WITH BASE64 LOGO
# ==============================
st.markdown(
    f"""
    <div class="title-bar">
        <img src="data:image/png;base64,{logo_base64}" class="title-logo" alt="Company Logo">
        <div class="title-center">
            <h1>🤖 AI ICP Fit Evaluator</h1>
            <p>Evaluate  profiles, resumes, and job descriptions for ICP fit using <b>AI</b>.</p>
        </div>
        <div style="width:65px;"></div>
    </div>
    """,
    unsafe_allow_html=True
)

#st.info("✅ Gemini API key loaded successfully from `.env`")

# ==============================
# INPUT SECTIONS
# ==============================
#st.markdown("<div class='section-card'>", unsafe_allow_html=True)
st.subheader("👤 Candidate Information")
_url = st.text_input("🔗  Profile URL (optional):")
if _url:
    st.warning("⚠️ As of now,  profile s cannot be read automatically. Please paste the profile text below or upload a resume instead.")

_text = st.text_area("💬 Paste  'About' Section Text (or Summary):", value=st.session_state.get("_text", ""), height=150)
resume_file = st.file_uploader("📄 Upload Resume (optional)", type=["txt", "pdf"])
st.markdown("</div>", unsafe_allow_html=True)

#st.markdown("<div class='section-card'>", unsafe_allow_html=True)
st.subheader("💼 Job Description")
jd_text = st.text_area("🧾 Paste Job Description (JD):", height=150)
jd_file = st.file_uploader("📎 Or Upload JD File (optional)", type=["txt", "pdf"])
st.markdown("</div>", unsafe_allow_html=True)

# ==============================
# MAIN EVALUATION
# ==============================
if st.button("🚀 Evaluate Fit", use_container_width=True, type="primary"):
    jd_final = jd_text or read_file(jd_file)
    resume_text = read_file(resume_file)

    if not jd_final:
        st.error("Please provide a Job Description (JD).")
    elif not _text and not resume_text:
        st.error("Please provide  text or upload a resume.")
    else:
        with st.spinner("Analyzing candidate fit... ⏳"):
            prompt = f"""
            You are an AI evaluator that determines whether a candidate fits an Ideal Customer Profile (ICP)
            for a given job description.

            Rules/Criteria:
            {json.dumps(rules, indent=2)}

            Job Description (JD):
            {jd_final}

            Candidate Data:
             Text: {_text}
            Resume Text: {resume_text}

            Task:
            - Compare the candidate’s background with the JD and ICP rules.
            - Return this output format:
              Fit Status: Fit / Not Fit
              Reason (2–3 sentences)
            """

            try:
                genai.configure(api_key=GOOGLE_API_KEY)
                model = genai.GenerativeModel("gemini-2.5-flash")
                response = model.generate_content(prompt)
                st.markdown("<div class='output-card'>", unsafe_allow_html=True)
                st.success("✅ Evaluation Complete")
                st.markdown(response.text)
                st.markdown("</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ API Error: {e}")

# ==============================
# FOOTER
# ==============================
st.markdown(
    """
    <div style='text-align:center; color:#555; margin-top:25px;'>
        <hr style="border: none; height: 2px; background: linear-gradient(to right, #1976d2, #42a5f5); margin: 20px 0;">
        <p>✨ Designed by <b> Taviti Naidu </b> || IncubXperts 🚀</p>
    </div>
    """,
    unsafe_allow_html=True
)
