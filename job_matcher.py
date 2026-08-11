def extract_job_skills(job_description):

    with open(
        "data/skills.csv",
        "r"
    ) as file:

        skills = file.read().splitlines()


    found_skills = []


    for skill in skills:

        if skill.lower() in job_description.lower():

            found_skills.append(skill)


    return found_skills