import streamlit as st
from PIL import Image
import os
import base64

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Abinaya S | Portfolio",
    layout="wide"
)

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, "profile.jpg")
RESUME = os.path.join(BASE, "resume.pdf")

# ---------------- GLOBAL STYLES ----------------
st.markdown("""
<style>
/* Global font & color */
html, body, p, li, span, div {
    font-size: 20px !important;
    color: #111827 !important;
    line-height: 1.9 !important;
}

/* Headings with colorful inside borders */
h1, h2, h3 {
    display: inline-block;
    padding: 8px 20px;
    border-radius: 12px;
    border: 3px solid;
    border-image-slice: 1;
    border-image-source: linear-gradient(90deg, #ff6b6b, #f0932b, #6ab04c, #22d3ee, #a78bfa, #fb7185);
    color: #111827 !important;
    font-weight: 700;
    margin-bottom: 20px;
}

/* Profile image */
.profile-img {
    width: 260px;
    height: 260px;
    border-radius: 50%;
    object-fit: cover;
    border: 7px solid transparent;
    background:
      linear-gradient(#05080f,#05080f) padding-box,
      linear-gradient(135deg,#22d3ee,#a78bfa,#fb7185) border-box;
    box-shadow: 0 0 50px rgba(168,85,247,0.9);
}

/* Tags */
.tag {
    display:inline-block;
    padding:8px 18px;
    border-radius:999px;
    background:#020617;
    color:#7dd3fc;
    font-size:15px;
    margin:8px 8px 8px 0;
    font-weight:600;
}

/* Section container */
.section {
    padding: 40px 0;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.title("📌 Navigate")
section = st.sidebar.radio(
    "Go to",
    (
        "About Me",
        "Skills",
        "Internships",
        "Certifications",
        "Education",
        "Contact"
    )
)

# ---------------- ABOUT ----------------
if section == "About Me":
    st.markdown("<h1>👩‍💻 About Me</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    with col1:
        # Display profile image with gradient border
        img_bytes = open(IMG, "rb").read()
        st.markdown(
            f'<img src="data:image/jpeg;base64,{base64.b64encode(img_bytes).decode()}" class="profile-img">',
            unsafe_allow_html=True
        )

    with col2:
        st.write("""
I am an enthusiastic **Artificial Intelligence & Data Science undergraduate**
with a strong passion for applying technology to solve real-world problems.

I have gained solid fundamentals in **Python, Data Science, and AI concepts**
through academic learning, internships, and hands-on workshops.

I actively seek opportunities to enhance my technical skills,
gain industry exposure, and grow into a skilled AI professional.
""")
        with open(RESUME, "rb") as f:
            st.download_button(
                label="📄 Download Resume",
                data=f,
                file_name="Abinaya_Resume.pdf",
                mime="application/pdf"
            )

# ---------------- SKILLS ----------------
elif section == "Skills":
    st.markdown("<h1>🧠 Skills & Expertise</h1>", unsafe_allow_html=True)

    st.markdown("<h2>🐍 Python Programming</h2>", unsafe_allow_html=True)
    st.write("Strong command in Python for problem solving, scripting, data handling, and AI-based implementations.")
    st.progress(85)

    st.markdown("<h2>📊 Data Science & Analytics</h2>", unsafe_allow_html=True)
    st.write("Experience in data preprocessing, analysis, and visualization using Pandas and real-world datasets.")
    st.progress(80)

    st.markdown("<h2>🤖 Artificial Intelligence & Machine Learning</h2>", unsafe_allow_html=True)
    st.write("Good understanding of AI–ML fundamentals, learning models, and real-world applications.")
    st.progress(75)

    st.markdown("<h2>🌐 Web Development</h2>", unsafe_allow_html=True)
    st.write("Hands-on experience in HTML and CSS for building responsive and user-friendly web pages.")
    st.progress(70)

    st.markdown("<h2>🤝 Soft Skills</h2>", unsafe_allow_html=True)
    st.write("Strong communication, teamwork, adaptability, and analytical thinking.")
    st.progress(90)

# ---------------- INTERNSHIPS ----------------
elif section == "Internships":
    st.markdown("<h1>🏢 Internships & Workshops</h1>", unsafe_allow_html=True)

    st.markdown("<h2>Tech Power Solutions, Chennai</h2>", unsafe_allow_html=True)
    st.write("**AI Using Python – June 2025**\nWorked on Artificial Intelligence concepts using Python. Learned data preprocessing, AI workflows, and real-world application understanding.")

    st.markdown("<h2>CodeBind Technologies, Chennai</h2>", unsafe_allow_html=True)
    st.write("**Web Development – July 2024**\nGained hands-on experience in frontend development. Designed responsive web pages and learned professional web practices.")

    st.markdown("<h2>ALTAIR – Data Science Master (Virtual Internship)</h2>", unsafe_allow_html=True)
    st.write("**Jan – Mar 2025**\nFocused on data analytics, visualization, and real-world dataset interpretation with mentor guidance.")

    st.markdown("<h2>India Edu Program – AI & ML Virtual Internship</h2>", unsafe_allow_html=True)
    st.write("**Oct – Dec 2024**\nLearned AI–ML fundamentals, industry use cases, and application-based learning through structured modules.")

# ---------------- CERTIFICATIONS ----------------
elif section == "Certifications":
    st.markdown("<h1>📜 Certifications & Learning</h1>", unsafe_allow_html=True)

    st.markdown("<h2>☁ AWS Academy – Cloud Architecture</h2>", unsafe_allow_html=True)
    st.write("Completed training on cloud computing fundamentals including cloud services, deployment models, and basic cloud architecture concepts.")

    st.markdown("<h2>🤖 Machine Learning Using Python</h2>", unsafe_allow_html=True)
    st.write("Gained practical knowledge of machine learning concepts using Python. Learned about data preprocessing, basic algorithms, and real-world applications.")

    st.markdown("<h2>🗄 MongoDB Basics</h2>", unsafe_allow_html=True)
    st.write("Learned NoSQL database fundamentals including collections, documents, and CRUD operations.")

    st.markdown("<h2>🧠 Human Computer Interaction – NPTEL</h2>", unsafe_allow_html=True)
    st.write("Studied principles of user-centered design, usability, and human interaction with systems.")

    st.markdown("<h2>🌐 Internet of Things – NPTEL</h2>", unsafe_allow_html=True)
    st.write("Learned the basics of IoT architecture, sensors, devices, and real-world IoT applications.")

# ---------------- EDUCATION ----------------
elif section == "Education":
    st.markdown("<h1>🎓 Education</h1>", unsafe_allow_html=True)

    st.write("""
**B.Tech – Artificial Intelligence & Data Science**  
Dhanalakshmi Srinivasan Engineering College  
CGPA: **8.55** (2022 – 2026)
""")

# ---------------- CONTACT ----------------
elif section == "Contact":
    st.markdown("<h1>📞 Contact</h1>", unsafe_allow_html=True)

    st.write("""
📧 **Email:** abinayaselvam205@gmail.com  
📱 **Phone:** 6382642968  
📍 **Location:** Thanjavur, Tamil Nadu
""")

st.markdown("---")
st.markdown("✨ *Designed & Developed by **Abinaya S***")
