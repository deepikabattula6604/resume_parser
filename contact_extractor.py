import re


def extract_email(text):

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    result = re.search(email_pattern, text)

    if result:
        return result.group()

    return None



def extract_phone(text):

    phone_pattern = r"\+?\d[\d\s-]{9,}"

    result = re.search(phone_pattern, text)

    if result:
        return result.group()

    return None



def extract_name(text):

    lines = text.split("\n")

    # First line of resume usually contains name
    return lines[0].strip()