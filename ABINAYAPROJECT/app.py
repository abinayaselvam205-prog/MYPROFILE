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

/* Global text style */
html, body, p, li, span, div {
    font-size: 20px !important;
    color: #111827 !important;
    line-height: 1.8 !important;
}

/* Colorful inside-border headings */
h1, h2 {
    display: inline-block;
    padding: 10px 22px;
    border-radius: 14px;
    border: 3px solid;
    border-image-slice: 1;
    border-image-source: linear-gradient(
        90deg,
        #ff6b6b,
        #f0932b,
        #6ab04c,
        #22d3ee,
        #a78bfa,
        #fb7185
    );
    font-weight: 700;
    margin-bottom: 18px;
}

/* Profile image style */
.profile-img {
    width: 260px;
    height: 260px;
    border-radius: 50%;
    object-fit: cover;
    border: 7px solid transparent;
    background:
      linear-gradient(#05080f,#05080f) padding-box,
      linear-gradient(135deg,#22d3ee,#a78bfa,#fb7185) border-box;
    box-shadow: 0 0 45px rgba(168,85,247,0.8);
}

/* Education timeline card */
.edu-card {
    border-left: 6px solid;
    border-image-slice: 1;
    border-image-source: linear-gradient(180deg, #22d3ee, #a78bfa, #fb7185);
    padding: 18px 25px;
    margin: 25px 0;
    background: #f9fafb;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Navigate")
section = st.sidebar.radio(
    "Go to",
    (
        "About Me",
        "Skills",
        "Internships & Workshops",
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
        img_bytes = open(IMG, "rb").read()
        st.markdown(
            f'<img src="data:image/jpeg;base64,{base64.b64encode(img_bytes).decode()}" class="profile-img">',
            unsafe_allow_html=True
        )

    with col2:
        st.write("""
I am an enthusiastic **Artificial Intelligence & Data Science undergraduate**
with a strong passion for applying technology to solve real-world problems.

I have gained solid foundations in **Python, Data Science, Artificial Intelligence,
and Machine Learning** through academic learning, internships, and hands-on workshops.

I am highly motivated to enhance my technical expertise,
gain industry exposure, and grow into a skilled AI professional.
""")

        with open(RESUME, "rb") as f:
            st.download_button(
                "📄 Download Resume",
                f,
                "Abinaya_Resume.pdf",
                mime="application/pdf"
            )

# ---------------- SKILLS ----------------
elif section == "Skills":
    st.markdown("<h1>🧠 Skills & Expertise</h1>", unsafe_allow_html=True)

    st.markdown("<h2>🐍 Python Programming</h2>", unsafe_allow_html=True)
    st.write("Strong command in Python for problem-solving, scripting, data handling, and AI-based implementations.")
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
elif section == "Internships & Workshops":
    st.markdown("<h1>🏢 Internships & Workshops</h1>", unsafe_allow_html=True)

    st.markdown("<h2>Tech Power Solutions, Chennai</h2>", unsafe_allow_html=True)
    st.write("""
**AI Using Python – June 2025**

• Learned core Artificial Intelligence concepts using Python  
• Worked with real-time datasets and AI workflows  
• Gained hands-on experience in Python-based AI problem solving  
• Improved analytical and logical thinking skills
""")

    st.markdown("<h2>CodeBind Technologies, Chennai</h2>", unsafe_allow_html=True)
    st.write("""
**Web Development – July 2024**

• Designed responsive web pages using HTML and CSS  
• Learned webpage layouts, styling techniques, and UI principles  
• Understood professional frontend development practices  
• Improved creativity and web presentation skills
""")

    st.markdown("<h2>ALTAIR – Data Science Master (Virtual Internship)</h2>", unsafe_allow_html=True)
    st.write("""
**January – March 2025**

• Performed data preprocessing and analysis using Pandas and NumPy  
• Worked on data visualization and interpretation  
• Learned real-world dataset handling with mentor guidance  
• Gained industry-oriented data science exposure
""")

    st.markdown("<h2>India Edu Program – AI & ML Virtual Internship</h2>", unsafe_allow_html=True)
    st.write("""
**October – December 2024**

• Learned AI & ML fundamentals with real-world use cases  
• Understood supervised and unsupervised learning concepts  
• Completed structured learning modules and assessments  
• Strengthened conceptual knowledge in AI & ML technologies
""")

# ---------------- CERTIFICATIONS ----------------
elif section == "Certifications":
    st.markdown("<h1>📜 Certifications & Learning</h1>", unsafe_allow_html=True)

    st.markdown("<h2>☁ AWS Academy – Cloud Architecture</h2>", unsafe_allow_html=True)
    st.write("""
• Learned cloud computing fundamentals and AWS services  
• Understood cloud deployment models and architecture  
• Gained knowledge of scalability, security, and infrastructure  
• Built foundational understanding of cloud-based systems
""")

    st.markdown("<h2>🤖 Machine Learning Using Python</h2>", unsafe_allow_html=True)
    st.write("""
• Learned machine learning concepts and algorithms  
• Worked on data preprocessing and model basics  
• Understood supervised and unsupervised learning  
• Applied Python libraries for ML implementation
""")

    st.markdown("<h2>🗄 MongoDB Basics</h2>", unsafe_allow_html=True)
    st.write("""
• Learned NoSQL database fundamentals  
• Worked with collections and documents  
• Performed CRUD operations  
• Understood database usage in applications
""")

    st.markdown("<h2>🧠 Human Computer Interaction – NPTEL</h2>", unsafe_allow_html=True)
    st.write("""
• Studied user-centered design principles  
• Learned usability engineering concepts  
• Understood human–computer interaction models  
• Improved UI/UX awareness
""")

    st.markdown("<h2>🌐 Internet of Things (IoT) – NPTEL</h2>", unsafe_allow_html=True)
    st.write("""
• Learned IoT architecture and components  
• Studied sensors, devices, and smart systems  
• Understood real-world IoT applications  
• Gained conceptual knowledge of connected technologies
""")

# ---------------- EDUCATION ----------------
elif section == "Education":
    st.markdown("<h1>🎓 Education</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="edu-card">
        <b>2022 – 2026</b><br>
        <b>Bachelor of Technology (Artificial Intelligence & Data Science)</b><br>
        Dhanalakshmi Srinivasan Engineering College (Autonomous)<br>
        CGPA: <b>8.55</b>
    </div>

    <div class="edu-card">
        <b>2021 – 2022</b><br>
        <b>Higher Secondary Certificate (HSC)</b><br>
        Government Higher Secondary School<br>
        Percentage: <b>72.3%</b>
    </div>

    <div class="edu-card">
        <b>2019 – 2020</b><br>
        <b>SSLC</b><br>
        Government Higher Secondary School<br>
        Percentage: <b>83.4%</b>
    </div>
    """, unsafe_allow_html=True)

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







