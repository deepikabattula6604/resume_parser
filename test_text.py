from extractors.text_extractor import extract_text

resume_text = extract_text("resumes/sample_resume.pdf")

print(resume_text)