def extract_certifications(text):

    certifications = []


    if "CERTIFICATIONS" not in text:
        return certifications


    cert_text = text.split("CERTIFICATIONS")[1]


    # Stop before next section
    sections = [
        "ACHIEVEMENTS",
        "WORKSHOPS"
    ]


    for section in sections:
        if section in cert_text:
            cert_text = cert_text.split(section)[0]


    lines = [
        line.strip()
        for line in cert_text.split("\n")
        if line.strip()
    ]


    for line in lines:

        if line.startswith("•"):

            certifications.append(
                line.replace("•", "").strip()
            )


    return certifications