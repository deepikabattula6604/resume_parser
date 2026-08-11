from extractors.text_extractor import extract_text
from extractors.projects_extractor import extract_projects


text = extract_text(
    "resumes/sample_resume.pdf"
)


projects = extract_projects(text)


print("Projects:")

for project in projects:
    print(project)
    