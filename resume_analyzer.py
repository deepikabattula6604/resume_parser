def analyze_resume(data):

    strengths = []

    weaknesses = []

    suggestions = []


    # Get skills safely

    skills = [
        skill.lower()
        for skill in data.get("skills", [])
    ]


    projects = data.get(
        "projects",
        []
    )


    experience = data.get(
        "experience",
        []
    )



    # ==========================
    # Strength Analysis
    # ==========================


    if "python" in skills:

        strengths.append(
            "Strong Python programming skills"
        )


    if "machine learning" in skills:

        strengths.append(
            "Machine Learning experience"
        )


    if "generative ai" in skills:

        strengths.append(
            "Knowledge of Generative AI technologies"
        )


    if len(projects) >= 3:

        strengths.append(
            "Good project experience"
        )


    if len(experience) >= 1:

        strengths.append(
            "Has internship experience"
        )



    # ==========================
    # Weakness Analysis
    # ==========================


    if "sql" not in skills:

        weaknesses.append(
            "SQL skill is missing"
        )


    if "aws" not in skills:

        weaknesses.append(
            "Cloud knowledge (AWS) is missing"
        )


    if "docker" not in skills:

        weaknesses.append(
            "Docker skill is missing"
        )


    if "react" not in skills:

        weaknesses.append(
            "React frontend framework knowledge is missing"
        )


    if "data structures" not in skills:

        weaknesses.append(
            "Data Structures and Algorithms knowledge is not mentioned"
        )



    # ==========================
    # Suggestions
    # ==========================


    for item in weaknesses:

        suggestions.append(
            "Improve: " + item
        )


    suggestions.extend([

        "Build more real-world AI projects",

        "Improve problem solving skills",

        "Practice coding interview questions"

    ])



    # ==========================
    # Final Result
    # ==========================


    return {


        "strengths": strengths,


        "weaknesses": weaknesses,


        "suggestions": suggestions

    }