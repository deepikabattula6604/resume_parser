from ats.job_matcher import extract_job_skills
from ats.ats_score import calculate_ats_score



resume_skills = [
    "Python",
    "Machine Learning",
    "Git",
    "HTML"
]


with open(
    "data/job_description.txt",
    "r"
) as file:

    job_description = file.read()



job_skills = extract_job_skills(
    job_description
)



result = calculate_ats_score(
    resume_skills,
    job_skills
)



print(result)