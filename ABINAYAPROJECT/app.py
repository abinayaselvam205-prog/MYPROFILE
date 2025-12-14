import streamlit as st
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Abinaya S | Portfolio", layout="wide")

# ---------------- CSS DESIGN ----------------
st.markdown("""
<style>
html { scroll-behavior: smooth; }
body { background: #f8f9fa; font-family: 'Arial', sans-serif; }

.navbar {
    display: flex;
    justify-content: center;
    gap: 40px;
    padding: 15px 20px;
    background: #ffffffcc;
    backdrop-filter: blur(10px);
    border-radius: 12px;
    margin-bottom: 40px;
    border: 1px solid #d4d4d4;
    position: sticky;
    top: 0;
    z-index: 100;
}
.navbar a {
    text-decoration: none;
    font-size: 18px;
    font-weight: 600;
    color: #333;
    transition: color 0.3s;
}
.navbar a:hover { color: #6c63ff; }

.section-title {
    font-size: 32px;
    font-weight: 700;
    color: #6c63ff;
    margin-top: 50px;
    margin-bottom: 20px;
    text-align: center;
}

.contact-icons img {
    width: 40px;
    margin-right: 12px;
    cursor: pointer;
    transition: transform 0.3s ease;
}
.contact-icons img:hover { transform: scale(1.3); }

.resume-btn {
    background: linear-gradient(90deg, #6c63ff, #9f7eff);
    color: white;
    padding: 10px 20px;
    border-radius: 12px;
    font-weight: 600;
    text-decoration: none;
}
.resume-btn:hover { opacity: 0.9; }
</style>
""", unsafe_allow_html=True)

# ---------------- NAVBAR ----------------
st.markdown("""
<div class="navbar">
<a href="#about">About</a>
<a href="#skills">Skills</a>
<a href="#projects">Mini Project</a>
<a href="#internships">Internships</a>
<a href="#certifications">Certifications</a>
<a href="#education">Education</a>
<a href="#contact">Contact</a>
</div>
""", unsafe_allow_html=True)

# ---------------- ABOUT SECTION ----------------
st.markdown("<div id='about'></div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "profile.jpg")

img = Image.open(image_path)
st.image(img, width=220)

    

with col2:
    st.title("Abinaya S")
    st.write("📍 Edaiyathi Maligaipunjai, Thanjavur")
    st.write("""
A dedicated and motivated individual with strong interest in technology,  
artificial intelligence, data science, and software development.  
Eager to learn, build, and contribute to impactful tech projects.
""")

    # Resume Download
    resume_path = os.path.join(BASE_DIR, "resume.pdf")

try:
    with open(resume_path, "rb") as f:
        st.download_button(
            "📄 Download Resume",
            f,
            "Abinaya_Resume.pdf",
            key="resume"
        )
except FileNotFoundError:
    st.warning("⚠️ Resume not found — upload `resume.pdf` in the app folder")

    # Social Icons
    st.markdown("""
    <div class='contact-icons' style='margin-top:20px;'>
        <a href="#" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
        </a>
        <a href="#" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733609.png">
        </a>
        <a href="mailto:abinayaselvam205@gmail.com" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png">
        </a>
    </div>
    """, unsafe_allow_html=True)

# ---------------- SKILLS ----------------
st.markdown("<div id='skills' class='section-title'>Skills</div>", unsafe_allow_html=True)

colA, colB, colC = st.columns(3)

with colA:
    st.markdown("""
**Technical Skills:**  
- Python  
- C Programming  
- HTML  
- CSS  
- Pandas  
- Computer Skills  
""")

with colB:
    st.markdown("""
**Soft Skills:**  
- Teamwork  
- Problem Solving  
- Fast Learner  
- Goal-oriented  
- Multitasking  
""")

with colC:
    st.markdown("""
**Languages Known:**  
- English  
- Tamil  
""")

# ---------------- MINI PROJECT ----------------
st.markdown("<div id='projects' class='section-title'>Mini Project</div>", unsafe_allow_html=True)

st.markdown("""
### 🌾 Crop Recommendation System using Python  
**Institution:** Dhanalakshmi Srinivasan Engineering College, Perambalur  

Machine learning model that recommends the best crop based on:
- Soil nutrients (N, P, K)  
- Temperature  
- Humidity  
- pH  
- Rainfall  

**Abstract:**  
This ML-based system helps farmers choose the most suitable crop,  
enhancing smart farming and improving agricultural productivity.
""")

# ---------------- INTERNSHIPS ----------------
st.markdown("<div id='internships' class='section-title'>Internships</div>", unsafe_allow_html=True)

st.write("""
**Intern – Tech Power Solutions, Chennai**  
📅 June 2025  
🧠 *AI Using Python*
""")

st.write("""
**Intern – CodeBind Technologies, Chennai**  
📅 July 2024  
💻 *Web Development*
""")

# ---------------- CERTIFICATIONS ----------------
st.markdown("<div id='certifications' class='section-title'>Certifications</div>", unsafe_allow_html=True)

st.write("""
- AWS Academy Cloud Architecture – Course Completion  
- Machine Learning Using Python – AI Foundation  
- MongoDB Basics – Course Completion  
- Human Computer Interaction – NPTEL  
- Internet of Things – NPTEL  
""")

# ---------------- EDUCATION ----------------
st.markdown("<div id='education' class='section-title'>Education</div>", unsafe_allow_html=True)

st.write("""
**Bachelor of Technology – Artificial Intelligence & Data Science**  
Dhanalakshmi Srinivasan Engineering College (Autonomous), Perambalur  
📅 2022 – 2026  
📊 CGPA: **8.55**
""")

st.write("""
**Higher Secondary (HSC)**  
Government Higher Secondary School  
📅 2021 – 2022  
📊 Percentage: **72.3%**
""")

st.write("""
**SSLC**  
Government Higher Secondary School  
📅 2019 – 2020  
📊 Percentage: **83.4%**
""")

# ---------------- CONTACT ----------------
st.markdown("<div id='contact' class='section-title'>Contact</div>", unsafe_allow_html=True)

st.write("📧 **Email:** abinayaselvam205@gmail.com")
st.write("📱 **Phone:** 6382642968")
st.write("📍 **Address:** Edaiyathi Maligaipunjai, Thanjavur")

# ---------------- FOOTER ----------------
st.markdown("""<hr><center>Made with ❤️ by <b>Abinaya S</b></center>""", unsafe_allow_html=True)
