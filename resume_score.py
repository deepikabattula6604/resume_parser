def calculate_resume_score(data):

    score = 0


    # =========================
    # Skills Score
    # =========================

    skills = data.get(
        "skills",
        []
    )


    if len(skills) >= 5:
        score += 20



    # =========================
    # Projects Score
    # =========================

    projects = data.get(
        "projects",
        []
    )


    if len(projects) >= 3:
        score += 20



    # =========================
    # Experience Score
    # =========================

    experience = data.get(
        "experience",
        []
    )


    if len(experience) >= 1:
        score += 20



    # =========================
    # Certifications Score
    # =========================

    certifications = data.get(
        "certifications",
        []
    )


    if len(certifications) >= 3:
        score += 20



    # =========================
    # ATS Score
    # =========================

    ats = data.get(
        "ats",
        {}
    )


    ats_score = ats.get(
        "score",
        0
    )


    score += int(
        ats_score * 0.2
    )


    return score