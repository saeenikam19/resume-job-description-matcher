"""
Project 4: Resume and Job Description Matcher
Skills: Python, NLP text processing, TF-IDF, cosine similarity, keyword matching.
This is a simple matching aid, NOT an ATS score or a hiring decision.
Install: pip install scikit-learn
Run: python 04_resume_job_matcher.py
"""
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS = [
    "python", "sql", "pandas", "numpy", "scikit-learn", "machine learning",
    "deep learning", "tensorflow", "pytorch", "nlp", "llm", "rag",
    "fastapi", "flask", "git", "github", "power bi", "tableau",
    "data analysis", "statistics", "docker", "aws", "azure", "streamlit",
    "classification", "regression", "feature engineering", "model evaluation"
]

def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\s-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

def extract_skills(text):
    normalized = normalize(text)
    found = []
    for skill in SKILLS:
        pattern = r"(?<![a-z0-9])" + re.escape(skill) + r"(?![a-z0-9])"
        if re.search(pattern, normalized):
            found.append(skill)
    return sorted(set(found))

def main():
    print("Paste your resume text below. Finish with a line containing END:")
    resume_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        resume_lines.append(line)
    resume = "\\n".join(resume_lines).strip()

    print("\\nPaste the job description below. Finish with a line containing END:")
    job_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        job_lines.append(line)
    job = "\\n".join(job_lines).strip()

    if not resume or not job:
        print("Both resume and job description are required.")
        return

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
    matrix = vectorizer.fit_transform([resume, job])
    similarity = float(cosine_similarity(matrix[0:1], matrix[1:2])[0, 0])

    resume_skills = set(extract_skills(resume))
    job_skills = set(extract_skills(job))
    matched = sorted(resume_skills & job_skills)
    missing = sorted(job_skills - resume_skills)

    print("\\n--- MATCH REPORT ---")
    print(f"Text similarity: {similarity:.1%}")
    print("Note: similarity is not a probability of being hired.")
    print("\\nDetected skills in resume:", ", ".join(sorted(resume_skills)) or "None detected")
    print("Detected skills in job description:", ", ".join(sorted(job_skills)) or "None detected")
    print("Matching skills:", ", ".join(matched) or "None detected")
    print("Job skills not detected in resume:", ", ".join(missing) or "None detected")

    with open("resume_job_match_report.txt", "w", encoding="utf-8") as file:
        file.write("Resume and Job Description Match Report\\n")
        file.write(f"Text similarity: {similarity:.1%}\\n")
        file.write("Matching skills: " + ", ".join(matched) + "\\n")
        file.write("Job skills not detected in resume: " + ", ".join(missing) + "\\n")
    print("\\nSaved resume_job_match_report.txt")

if __name__ == "__main__":
    main()
