import re
from collections import Counter

import fitz  # PyMuPDF
import streamlit as st


# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
)

# ------------------------------------------------------------
# SKILL DATABASE
# Add more skills here whenever needed.
# ------------------------------------------------------------
SKILLS = [
    "python", "java", "c", "c++", "c#", "javascript", "html", "css",
    "sql", "mysql", "mongodb", "postgresql", "excel", "power bi",
    "tableau", "pandas", "numpy", "matplotlib", "seaborn", "plotly",
    "machine learning", "deep learning", "artificial intelligence",
    "data analysis", "data analytics", "data visualization",
    "natural language processing", "nlp", "scikit-learn", "tensorflow",
    "pytorch", "streamlit", "flask", "django", "git", "github",
    "aws", "azure", "google cloud", "docker", "kubernetes",
    "selenium", "testing", "communication", "problem solving",
    "project management", "rest api", "api", "linux",
]

# Role names and the skills commonly requested for those roles.
JOB_ROLES = {
    "Python Developer": [
        "python", "sql", "git", "github", "rest api", "django", "flask",
        "problem solving",
    ],
    "Data Analyst": [
        "python", "sql", "excel", "power bi", "tableau", "pandas",
        "numpy", "data analysis", "data visualization",
    ],
    "Machine Learning Engineer": [
        "python", "machine learning", "deep learning", "pandas", "numpy",
        "scikit-learn", "tensorflow", "sql",
    ],
    "AI / NLP Engineer": [
        "python", "artificial intelligence", "machine learning",
        "natural language processing", "nlp", "deep learning",
        "tensorflow", "pytorch",
    ],
    "Web Developer": [
        "html", "css", "javascript", "python", "django", "flask",
        "rest api", "git",
    ],
    "Software Engineer": [
        "python", "java", "c++", "sql", "git", "github",
        "problem solving", "testing",
    ],
}

COURSES = {
    "python": "Python programming fundamentals",
    "java": "Java programming and OOP",
    "sql": "SQL and database fundamentals",
    "mysql": "MySQL database development",
    "excel": "Advanced Microsoft Excel",
    "power bi": "Power BI data analytics",
    "tableau": "Tableau data visualization",
    "pandas": "Python Pandas for data analysis",
    "numpy": "NumPy for numerical computing",
    "machine learning": "Machine learning fundamentals",
    "deep learning": "Deep learning with neural networks",
    "artificial intelligence": "Introduction to Artificial Intelligence",
    "natural language processing": "Natural Language Processing",
    "nlp": "NLP with Python",
    "scikit-learn": "Scikit-learn practical machine learning",
    "tensorflow": "TensorFlow for deep learning",
    "pytorch": "PyTorch fundamentals",
    "html": "HTML5 web development",
    "css": "CSS and responsive web design",
    "javascript": "JavaScript fundamentals",
    "django": "Django web development",
    "flask": "Flask application development",
    "git": "Git version control",
    "github": "GitHub project collaboration",
    "rest api": "REST API development",
    "selenium": "Selenium automation testing",
    "docker": "Docker fundamentals",
    "aws": "AWS cloud practitioner fundamentals",
    "communication": "Professional communication skills",
    "problem solving": "Problem-solving and coding practice",
}

# --------------------------------------------------
# MAIN STREAMLIT APPLICATION
# --------------------------------------------------

st.title("📄 AI Resume Analyzer")

st.subheader(
    "AI Resume Analyzer & Job Recommendation System"
)

st.success("Application is running successfully!")

st.write("Welcome! Upload your resume to analyse your skills.")

st.divider()

selected_role = st.selectbox(
    "Select Your Target Job Role",
    list(JOB_ROLES.keys())
)

uploaded_file = st.file_uploader(
    "Upload Your Resume PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    if st.button("Analyze Resume"):

        with fitz.open(
            stream=uploaded_file.getvalue(),
            filetype="pdf"
        ) as pdf:

            resume_text = ""

            for page in pdf:
                resume_text += page.get_text()

        if not resume_text.strip():

            st.error("No readable text found in this PDF.")

        else:

            clean_resume = re.sub(
                r'\s+',
                ' ',
                resume_text.lower()
            )

            found_skills = []

            for skill in SKILLS:

                pattern = (
                    r'(?<![a-z0-9])'
                    + re.escape(skill)
                    + r'(?![a-z0-9])'
                )

                if re.search(pattern, clean_resume):
                    found_skills.append(skill)

            found_skills = sorted(set(found_skills))

            required_skills = JOB_ROLES[selected_role]

            matched_skills = [
                skill for skill in required_skills
                if skill in found_skills
            ]

            missing_skills = [
                skill for skill in required_skills
                if skill not in found_skills
            ]

            ats_score = (
                len(matched_skills)
                / len(required_skills)
            ) * 100

            st.divider()

            st.header("📊 Resume Analysis Results")

            st.metric(
                "ATS Skill Match Score",
                f"{ats_score:.2f}%"
            )

            st.progress(int(ats_score))

            st.subheader("Extracted Skills")
            st.write(found_skills)

            st.subheader("Matched Skills")
            st.write(matched_skills)

            st.subheader("Missing Skills")
            st.write(missing_skills)

            st.subheader("🎓 Recommended Courses")

            for skill in missing_skills:

                if skill in COURSES:
                    st.write("📚 " + COURSES[skill])

            st.success("Resume analysis completed!")
    