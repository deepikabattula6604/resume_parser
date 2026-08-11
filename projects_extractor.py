def extract_projects(text):

    projects = []

    if "PROJECTS" not in text:
        return projects


    project_text = text.split("PROJECTS")[1]


    # Stop before certifications
    if "CERTIFICATIONS" in project_text:
        project_text = project_text.split("CERTIFICATIONS")[0]


    lines = [
        line.strip()
        for line in project_text.split("\n")
        if line.strip()
    ]


    current_project = None
    description = []


    for line in lines:

        # New project title
        if not line.startswith("•"):

            if current_project:

                projects.append({
                    "title": current_project,
                    "description": description
                })


            current_project = line
            description = []


        else:

            description.append(
                line.replace("•", "").strip()
            )


    # Add final project
    if current_project:

        projects.append({
            "title": current_project,
            "description": description
        })


    return projects