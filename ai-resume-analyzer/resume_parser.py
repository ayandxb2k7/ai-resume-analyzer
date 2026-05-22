import PyPDF2
import re

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_skills(text):
    skills_list = [
        "python","java","c++","flask","django",
        "machine learning","sql","html","css",
        "javascript","react","node","pandas","numpy"
    ]

    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if re.search(r'\b' + skill + r'\b', text):
            found_skills.append(skill)

    return found_skills
