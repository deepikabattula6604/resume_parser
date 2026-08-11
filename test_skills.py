from extractors.text_extractor import extract_text
from extractors.skills_extractor import extract_skills


text = extract_text(
    "resumes/sample_resume.pdf"
)


skills = extract_skills(text)


print("Skills Found:")
for skill in skills:
    print(skill)