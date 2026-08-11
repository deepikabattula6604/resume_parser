from extractors.text_extractor import extract_text
from extractors.education_extractor import extract_education


text = extract_text(
    "resumes/sample_resume.pdf"
)


education = extract_education(text)


print("Education:")

for item in education:
    print(item)