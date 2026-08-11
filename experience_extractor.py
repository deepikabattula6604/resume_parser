def extract_experience(text):

    experience = []

    if "INTERNSHIPS" not in text:
        return experience


    exp_text = text.split("INTERNSHIPS")[1]


    # Stop before projects
    if "PROJECTS" in exp_text:
        exp_text = exp_text.split("PROJECTS")[0]


    lines = [
        line.strip()
        for line in exp_text.split("\n")
        if line.strip()
    ]


    current_company = None
    description = []


    for line in lines:

        # Company/internship names usually don't start with bullet
        if not line.startswith("•"):

            if current_company:

                experience.append({
                    "company": current_company,
                    "description": description
                })


            current_company = line
            description = []


        else:

            description.append(
                line.replace("•","").strip()
            )


    # Add last company
    if current_company:

        experience.append({
            "company": current_company,
            "description": description
        })


    return experience