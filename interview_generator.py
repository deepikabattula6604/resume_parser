def generate_interview_questions(resume_data):


    questions = {


        "technical": [],

        "projects": [],

        "experience": [],

        "hr": []

    }



    # =========================
    # Technical Questions
    # =========================


    skills = resume_data.get(
        "skills",
        []
    )


    for skill in skills:


        questions["technical"].append(

            f"Explain your knowledge and practical experience with {skill}."

        )



    # Add common technical questions

    questions["technical"].extend([

        "Explain your machine learning projects.",

        "How does Python help in AI development?",

        "Explain the difference between supervised and unsupervised learning.",

        "What are the steps involved in building a machine learning model?"

    ])




    # =========================
    # Project Questions
    # =========================


    projects = resume_data.get(
        "projects",
        []
    )


    for project in projects:


        if isinstance(project, dict):


            title = project.get(
                "title",
                "your project"
            )


            questions["projects"].append(

                f"Explain your project '{title}'. What was your role and what challenges did you solve?"

            )


    # Common project questions

    questions["projects"].extend([

        "What technologies did you use in your projects?",

        "What challenges did you face while developing your project?",

        "How can you improve your project in future?"

    ])





    # =========================
    # Experience Questions
    # =========================


    experience = resume_data.get(
        "experience",
        []
    )


    for exp in experience:


        if isinstance(exp, dict):


            company = exp.get(
                "company",
                "your internship"
            )


            questions["experience"].append(

                f"What did you learn during your {company} experience?"

            )



    questions["experience"].extend([


        "Explain your internship responsibilities.",

        "What technologies did you use during your internship?",

        "How did your internship improve your technical skills?"

    ])






    # =========================
    # HR Questions
    # =========================


    questions["hr"] = [


        "Tell me about yourself.",


        "Why do you want this job role?",


        "What are your strengths?",


        "What are your weaknesses?",


        "Where do you see yourself after five years?",


        "Describe your biggest achievement.",


        "Why should we hire you?",


        "How do you handle challenges?",


        "Are you comfortable working in a team?"

    ]




    return questions