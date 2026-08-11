import pdfplumber

pdf_file = "resumes/sample_resume.pdf"

with pdfplumber.open(pdf_file) as pdf:

    print("Number of pages:", len(pdf.pages))

    for i, page in enumerate(pdf.pages):

        print("\n--- PAGE", i+1, "---")

        text = page.extract_text()

        print(text)