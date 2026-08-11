from ai.resume_analyzer import analyze_resume
from parser import parse_resume


data = parse_resume(
    "resumes/sample_resume.pdf"
)


result = analyze_resume(data)


print(result)