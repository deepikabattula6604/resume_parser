def load_skills():

    with open("data/skills.csv", "r") as file:
        skills = file.read().splitlines()

    return skills



def extract_skills(text):

    skills = load_skills()

    found_skills = []

    text = text.lower()

    for skill in skills:

        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))