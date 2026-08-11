def calculate_ats_score(resume_skills, job_skills):

    resume_skills = set(
        skill.lower()
        for skill in resume_skills
    )


    job_skills = set(
        skill.lower()
        for skill in job_skills
    )


    matched = resume_skills.intersection(job_skills)


    if len(job_skills) == 0:
        score = 0

    else:
        score = (
            len(matched)
            /
            len(job_skills)
        ) * 100


    return {
        "score": round(score,2),
        "matched_skills": list(matched),
        "missing_skills": list(
            job_skills - resume_skills
        )
    }