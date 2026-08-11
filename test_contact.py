from extractors.text_extractor import extract_text
from extractors.contact_extractor import extract_email
from extractors.contact_extractor import extract_phone
from extractors.contact_extractor import extract_name


text = extract_text("resumes/sample_resume.pdf")


print("Name:")
print(extract_name(text))


print("\nEmail:")
print(extract_email(text))


print("\nPhone:")
print(extract_phone(text))