from extractors.text_extractor import extract_text
from extractors.certifications_extractor import extract_certifications


text = extract_text(
    "resumes/sample_resume.pdf"
)


certifications = extract_certifications(text)


print("Certifications:")

for cert in certifications:
    print(cert)
    