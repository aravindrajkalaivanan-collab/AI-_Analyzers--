# 📄 AI Resume Analyzer & Job Recommendation System

## 📌 Project Overview

The **AI Resume Analyzer & Job Recommendation System** is a Python-based application developed using Streamlit. It helps students and job seekers analyse their resumes, identify skills, calculate an ATS-style skill matching score, and discover suitable job roles.

The system extracts text from uploaded PDF resumes and provides skill analysis, missing skill identification, job recommendations, and course suggestions.

## 🎯 Project Objectives

- Analyse resumes automatically using Python.
- Extract text from PDF resumes.
- Identify technical and professional skills.
- Calculate an ATS-style resume matching score.
- Identify missing skills based on the selected job role.
- Recommend suitable job roles.
- Suggest courses to improve missing skills.

## 🚀 Key Features

1. **PDF Resume Upload** – Upload resumes in PDF format.
2. **Text Extraction** – Extract resume content using PyMuPDF.
3. **Skill Extraction** – Identify skills using Python Regex.
4. **ATS Score Calculation** – Calculate skill matching percentage.
5. **Missing Skill Identification** – Find skills required for the selected role.
6. **Job Recommendations** – Recommend suitable job roles based on extracted skills.
7. **Course Recommendations** – Suggest learning courses for missing skills.
8. **Report Download** – Download resume analysis results.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| PyMuPDF | PDF text extraction |
| Regex | Text processing and skill extraction |
| Git & GitHub | Version control and project hosting |

## 💻 Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd AI_Resume_Analyzer
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Environment (Windows)

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install Required Packages

```bash
python -m pip install streamlit pymupdf
```

### Step 6: Run the Application

```bash
python -m streamlit run app.py2.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 📊 Application Workflow

1. User opens the Streamlit application.
2. Selects a target job role.
3. Uploads a PDF resume.
4. System extracts resume text.
5. Text is cleaned and processed.
6. Relevant skills are identified.
7. ATS-style skill matching score is calculated.
8. Missing skills are identified.
9. Suitable job roles are recommended.
10. Learning courses are suggested.
11. Analysis report can be downloaded.

## 🎯 Supported Job Roles

- Python Developer
- Data Analyst
- Machine Learning Engineer
- AI / NLP Engineer
- Web Developer
- Software Engineer

## 🔮 Future Enhancements

- MySQL database integration for storing resume analysis history.
- Power BI dashboard for resume analytics.
- Improved ATS scoring using advanced NLP techniques.
- Machine learning-based job recommendations.
- Resume improvement suggestions.
- User login and registration.
- Cloud deployment.

## 🎓 Academic Project

**Project Title:** AI Resume Analyzer & Job Recommendation System

**Department:** Artificial Intelligence and Data Science

**Project Type:** Final Year Academic Project

## 👨‍💻 Conclusion

This project aims to simplify
