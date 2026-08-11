from extractors.text_extractor import extract_text
from extractors.experience_extractor import extract_experience


text = extract_text(
    "resumes/sample_resume.pdf"
)


experience = extract_experience(text)


print("Experience:")

for item in experience:
    print(item)