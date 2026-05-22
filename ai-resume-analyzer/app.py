from flask import Flask, render_template, request
from resume_parser import extract_text_from_pdf, extract_skills
from similarity import calculate_similarity

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        file = request.files["resume"]
        job_desc = request.form["job_desc"]

        resume_text = extract_text_from_pdf(file)
        skills = extract_skills(resume_text)
        score = calculate_similarity(resume_text, job_desc)

        missing_skills = []
        job_desc_lower = job_desc.lower()

        for skill in skills:
            if skill not in job_desc_lower:
                missing_skills.append(skill)

        return render_template("result.html",
                               skills=skills,
                               score=score,
                               missing_skills=missing_skills)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
