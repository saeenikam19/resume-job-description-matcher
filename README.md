# Resume and Job Description Matcher

An NLP-based application that compares a resume with a job description and estimates how closely their textual content matches.

## Overview

Finding relevant job opportunities can be challenging when resumes and job descriptions contain different terminology. This project uses text processing and cosine similarity to measure the similarity between resume content and job requirements.

The tool is intended to help candidates identify relevant skills and keywords to review before applying.

## Objectives

- Process resume text and job descriptions.
- Clean and normalize textual data.
- Convert documents into numerical representations.
- Calculate similarity using cosine similarity.
- Identify potentially relevant keywords and skills.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- PyPDF2 or pypdf (optional, for PDF extraction)

## How It Works

1. Provide resume text or upload a supported resume file.
2. Enter or load a job description.
3. Extract text from both documents.
4. Clean and preprocess the text.
5. Convert the text into TF-IDF feature vectors.
6. Calculate cosine similarity between the vectors.
7. Display the similarity score and matching keywords.

## Core Concepts

**TF-IDF Vectorization**

Transforms resume and job-description text into numerical vectors that represent the importance of words.

**Cosine Similarity**

Measures the similarity between two numerical vectors. Higher similarity indicates greater overlap in their text representations.

The similarity score is not a probability of getting hired and should not be treated as a definitive ATS score.

## Example

**Resume skills:**
Python, SQL, Pandas, Machine Learning, Data Analysis

**Job requirements:**
Python, SQL, Machine Learning, Data Visualization, Statistics

The application compares the documents and reports their textual similarity. It can also highlight keywords that appear in one document but not the other.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/resume-job-description-matcher.git
cd resume-job-description-matcher
```

### 2. Install dependencies

```bash
pip install pandas numpy scikit-learn
```

For PDF resume extraction, install:

```bash
pip install pypdf
```

### 3. Run the project

```bash
python 04_resume_job_matcher.py
```

## Key Features

- Resume and job description comparison
- TF-IDF-based text representation
- Cosine similarity calculation
- Matching keyword identification
- Missing keyword suggestions
- Potential for batch comparison against multiple job descriptions

Features should be marked as implemented only after they are available in the code.

## Future Improvements

- Build a Streamlit interface.
- Support PDF and DOCX resumes.
- Extract technical skills into structured lists.
- Compare a resume against multiple job descriptions.
- Add semantic similarity using sentence embeddings.
- Generate suggestions for improving resume relevance.
- Keep uploaded resume content private and process it locally where possible.

## Limitations

Text similarity does not fully understand professional experience, skill proficiency, project quality, or hiring criteria. A low similarity score does not necessarily mean a candidate is unqualified.

## Learning Outcomes

- Natural language processing
- Text vectorization
- Cosine similarity
- Document comparison
- Keyword extraction
- Building practical NLP applications

## Author

Saee Nikam

