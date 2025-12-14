import streamlit as st
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

# ---------------- STYLES ----------------
st.markdown("""
<style>
html, body, p, li {
    font-size: 18px !important;
    color: #111827 !important;
    line-height: 1.7 !important;
}

/* Main heading */
.main-heading {
    display:inline-block;
    padding:8px 18px;
    border-radius:12px;
    border:3px solid;
    border-image-slice:1;
    border-image-source:linear-gradient(90deg,#ff6b6b,#f0932b,#22d3ee,#a78bfa,#fb7185);
    font-size:28px;
    font-weight:700;
    margin-bottom:20px;
}

/* Sub heading */
.sub-heading {
    display:inline-block;
    padding:6px 14px;
    border-radius:10px;
    border:2px solid;
    border-image-slice:1;
    border-image-source:linear-gradient(90deg,#22d3ee,#a78bfa,#fb7185);
    font-size:20px;
    font-weight:600;
    margin:14px 0 8px 0;
}

/* Profile image */
.profile-img {
    width:240px;
    height:240px;
    border-radius:50%;
    object-fit:cover;
    border:6px solid transparent;
    background:
      linear-gradient(#05080f,#05080f) padding-box,
      linear-gradient(135deg,#22d3ee,#a78bfa,#fb7185) border-box;
    box-shadow:0 0 35px rgba(168,85,247,0.7);
}

/* Education card */
.edu-card {
    border-left:5px solid;
    border-image-slice:1;
    border-image-source:linear-gradient(180deg,#22d3ee,#a78bfa,#fb7185);
    padding:16px 22px;
    margin:20px 0;
    background:#f9fafb;
    border-radius:12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Navigate")
section = st.sidebar.radio(
    "Go to",
    ("About Me","Skills","Internships","Workshops","Certifications","Education","Contact")
)

# ---------------- ABOUT ----------------
if section == "About Me":
    st.markdown("<div class='main-heading'>👩‍💻 About Me</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1,2])
    with col1:
        img = base64.b64encode(open(IMG,"rb").read()).decode()
        st.markdown(f"<img src='data:image/jpeg;base64,{img}' class='profile-img'>",
                    unsafe_allow_html=True)

    with col2:
        st.write("""
I am an enthusiastic **Artificial Intelligence & Data Science undergraduate**
with a strong interest in AI-driven problem solving.

I have developed solid fundamentals in **Python, Data Science, AI, and ML**
through internships, workshops, and academic learning.
""")
        with open(RESUME,"rb") as f:
            st.download_button("📄 Download Resume",f,"Abinaya_Resume.pdf")

# ---------------- SKILLS ----------------
elif section == "Skills":
    st.markdown("<div class='main-heading'>🧠 Skills</div>", unsafe_allow_html=True)

    st.markdown("<div class='sub-heading'>Python Programming</div>", unsafe_allow_html=True)
    st.write("Strong in logic building, scripting, and AI-based Python implementations.")
    st.progress(85)

    st.markdown("<div class='sub-heading'>Data Science & Analytics</div>", unsafe_allow_html=True)
    st.write("Experienced in data preprocessing, analysis, and visualization.")
    st.progress(80)

    st.markdown("<div class='sub-heading'>AI & Machine Learning</div>", unsafe_allow_html=True)
    st.write("Understanding of AI–ML concepts and real-world applications.")
    st.progress(75)

    st.markdown("<div class='sub-heading'>Web Development</div>", unsafe_allow_html=True)
    st.write("Hands-on experience with HTML and CSS for responsive design.")
    st.progress(70)

    st.markdown("<div class='sub-heading'>Soft Skills</div>", unsafe_allow_html=True)
    st.write("Communication, teamwork, adaptability, and problem solving.")
    st.progress(90)

# ---------------- INTERNSHIPS ----------------
elif section == "Internships":
    st.markdown("<div class='main-heading'>🏢 Internships</div>", unsafe_allow_html=True)

    st.markdown("<div class='sub-heading'>Tech Power Solutions – AI Using Python</div>", unsafe_allow_html=True)
    st.write("""
• Learned fundamentals of Artificial Intelligence concepts  
• Practiced Python programming for AI applications  
• Worked with basic AI models and logic building  
• Learned data preprocessing techniques  
• Implemented simple AI-based programs  
• Understood real-world AI workflows  
• Improved analytical and problem-solving skills  
• Gained industry-oriented AI exposure  
""")

    st.markdown("<div class='sub-heading'>CodeBind Technologies – Web Development</div>", unsafe_allow_html=True)
    st.write("""
• Learned basics of frontend web development  
• Designed web pages using HTML  
• Styled webpages using CSS  
• Created responsive layouts  
• Improved user interface design skills  
• Learned webpage structure and alignment  
• Practiced real-time web examples  
• Gained professional web exposure  
""")

    st.markdown("<div class='sub-heading'>ALTAIR – Data Science Master (Virtual)</div>", unsafe_allow_html=True)
    st.write("""
• Learned core data science concepts  
• Worked with real-world datasets  
• Performed data cleaning and preprocessing  
• Analyzed structured data  
• Used Python libraries for analysis  
• Learned data visualization techniques  
• Interpreted meaningful data insights  
• Gained practical data science experience  
""")

    st.markdown("<div class='sub-heading'>India Edu Program – AI & ML (Virtual)</div>", unsafe_allow_html=True)
    st.write("""
• Learned Artificial Intelligence fundamentals  
• Studied Machine Learning concepts  
• Understood supervised learning techniques  
• Learned unsupervised learning methods  
• Studied basic ML algorithms  
• Learned training and testing models  
• Explored real-world AI applications  
• Improved AI problem-solving skills  
""")

# ---------------- WORKSHOPS ----------------
elif section == "Workshops":
    st.markdown("<div class='main-heading'>🛠 Workshops</div>", unsafe_allow_html=True)

    st.markdown("<div class='sub-heading'>AI Using Python – IIT Madras</div>", unsafe_allow_html=True)
    st.write("""
• Learned basics of Artificial Intelligence  
• Implemented AI logic using Python  
• Studied intelligent problem-solving techniques  
• Learned basic AI algorithms  
• Practiced simple AI programs  
• Understood AI application concepts  
• Improved programming logic  
• Gained foundational AI exposure  
""")

    st.markdown("<div class='sub-heading'>Generative AI with Cloud – Kongu Engineering College</div>", unsafe_allow_html=True)
    st.write("""
• Learned fundamentals of Generative AI  
• Understood cloud-based AI services  
• Explored Generative AI tools  
• Learned prompt-based AI interaction  
• Studied real-world Generative AI use cases  
• Understood AI-cloud integration  
• Learned modern AI trends  
• Gained awareness of AI deployment  
""")

# ---------------- CERTIFICATIONS ----------------
elif section == "Certifications":
    st.markdown("<div class='main-heading'>📜 Certifications</div>", unsafe_allow_html=True)

    st.write("""
• AWS Academy – Cloud Architecture  
• Machine Learning Using Python  
• MongoDB Basics  
• NPTEL – Human Computer Interaction  
• NPTEL – Internet of Things  
""")

# ---------------- EDUCATION ----------------
elif section == "Education":
    st.markdown("<div class='main-heading'>🎓 Education</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="edu-card">
    <b>2022 – 2026</b><br>
    B.Tech – Artificial Intelligence & Data Science<br>
    Dhanalakshmi Srinivasan Engineering College (A)<br>
    CGPA: <b>8.55</b>
    </div>

    <div class="edu-card">
    <b>2021 – 2022</b><br>
    HSC – Government Higher Secondary School<br>
    Percentage: <b>72.3%</b>
    </div>

    <div class="edu-card">
    <b>2019 – 2020</b><br>
    SSLC – Government Higher Secondary School<br>
    Percentage: <b>83.4%</b>
    </div>
    """, unsafe_allow_html=True)

# ---------------- CONTACT ----------------
elif section == "Contact":
    st.markdown("<div class='main-heading'>📞 Contact</div>", unsafe_allow_html=True)
    st.write("""
📧 Email: abinayaselvam205@gmail.com  
📱 Phone: 6382642968  
📍 Location: Thanjavur, Tamil Nadu
""")

st.markdown("---")
st.markdown("✨ *Designed & Developed by **Abinaya S***")





