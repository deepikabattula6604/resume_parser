import re


def extract_education(text):

    education = []

    # Take only Education section
    if "EDUCATION" in text:

        education_text = text.split("EDUCATION")[1]

    else:
        return education


    # Stop at next section
    sections = [
        "TECHNICAL SKILLS",
        "INTERNSHIPS",
        "PROJECTS",
        "CERTIFICATIONS"
    ]

    for section in sections:
        if section in education_text:
            education_text = education_text.split(section)[0]


    lines = [
        line.strip()
        for line in education_text.split("\n")
        if line.strip()
    ]


    i = 0

    while i < len(lines):

        line = lines[i]


        if any(keyword in line.lower() for keyword in [
            "b.tech",
            "b.e",
            "bachelor",
            "m.tech",
            "mba",
            "intermediate",
            "ssc"
        ]):

            item = {
                "degree": line,
                "institution": "",
                "year": ""
            }


            if i + 1 < len(lines):
                item["institution"] = lines[i+1]


            # Search year only in nearby education lines
            nearby_text = " ".join(lines[i:i+3])


            year = re.search(
                r"\b(19|20)\d{2}\s*[-–]?\s*(19|20)?\d{0,4}\b",
                nearby_text
            )


            if year:
                item["year"] = year.group()


            education.append(item)


        i += 1


    return education