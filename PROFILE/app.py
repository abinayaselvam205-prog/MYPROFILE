import streamlit as st
from PIL import Image

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="Abinaya | Portfolio",
    page_icon="💼",
    layout="wide"
)

# ----------------- LOAD IMAGE -----------------
img = Image.open("photo.jpeg")



# ------------ HEADER SECTION -------------------
st.markdown("<h1 style='text-align:center; color:#1f4e79;'>💼 ABINAYA - PORTFOLIO</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.image(img, width=250)

with col2:
    st.markdown("""
    ### **B.Tech – Artificial Intelligence & Data Science (2022-2026)**
    **Dhanalakshmi Srinivasan Engineering College (Autonomous)**  
    **CGPA:** 8.55  
    """)

# Divider
st.markdown("---")

# ------------ EDUCATION -----------------------
st.subheader("🎓 EDUCATION")

st.markdown("""
**2022 – 2026**  
📌 *Bachelor of Technology (AI & DS)*  
Dhanalakshmi Srinivasan Engineering College(A)  
CGPA: **8.55**

**2021 – 2022**  
📌 *HSC*  
Government Hr. Sec. School  
Percentage: **72.3%**

**2019 – 2020**  
📌 *SSLC*  
Government Hr. Sec. School  
Percentage: **83.4%**
""")

st.markdown("---")

# ------------ SKILLS --------------------------
st.subheader("🛠️ SKILLS")

skills = [
    "Teamwork", "Problem-solving", "Fast learner", "Goal-oriented mindset",
    "Computer skills", "Multitasking", "HTML", "CSS", 
    "Python", "Pandas", "C Programming"
]

cols = st.columns(3)
i = 0
for skill in skills:
    cols[i].write(f"- {skill}")
    i = (i + 1) % 3

st.markdown("---")

# ------------ MINI PROJECT ---------------------
st.subheader("📌 MINI PROJECT")

st.markdown("""
### **Crop Recommendation System using Python & Machine Learning**

A machine-learning model that predicts the most suitable crop to grow based on:

- Soil nutrients (N, P, K)
- Temperature  
- Humidity  
- pH Level  
- Rainfall  

**Objective:** Assist farmers in smart farming and improve crop productivity.
""")

st.markdown("---")

# ------------ INTERNSHIPS ----------------------
st.subheader("💼 INTERNSHIPS")

st.markdown("""
- **Tech Power Solutions, Chennai (June 2025)**  
  *AI Using Python*
  
- **CodeBind Technologies, Chennai (July 2024)**  
  *Web Development*

- **Data Science Master Virtual Internship** – ALTAIR (Jan–Mar 2025)

- **AI-ML Virtual Internship** – India Edu Program (Oct–Dec 2024)
""")

st.markdown("---")

# ------------ COURSES --------------------------
st.subheader("📚 COURSES & CERTIFICATIONS")

st.markdown("""
- AWS Academy Cloud Architecture – Completion
- Machine Learning using Python – AI Foundation
- MongoDB Basics – Certificate
- Human Computer Interaction – NPTEL
- Internet of Things – NPTEL
""")

st.markdown("---")

# ------------ FOOTER ---------------------------
st.markdown("<h4 style='text-align:center;'>© 2025 Abinaya | Built with Streamlit</h4>", unsafe_allow_html=True)
