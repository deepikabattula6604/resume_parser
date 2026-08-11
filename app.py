from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename

from parser import parse_resume


app = Flask(__name__)


# ==========================
# Configuration
# ==========================

UPLOAD_FOLDER = "resumes"

ALLOWED_EXTENSIONS = {"pdf"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Create upload folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)



# ==========================
# File validation
# ==========================

def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )



# ==========================
# Home page
# ==========================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )



# ==========================
# Upload Resume
# ==========================

@app.route("/upload", methods=["POST"])
def upload():

    try:

        # Check file exists

        if "resume" not in request.files:

            return "No resume file uploaded"


        file = request.files["resume"]



        # Check filename

        if file.filename == "":

            return "No file selected"



        # Check PDF

        if not allowed_file(file.filename):

            return "Only PDF files are allowed"



        # Secure filename

        filename = secure_filename(
            file.filename
        )



        # Save file

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )


        file.save(file_path)



        print("File saved:", file_path)



        # Parse resume

        result = parse_resume(
            file_path
        )



        return render_template(
            "result.html",
            data=result
        )


    except Exception as e:

        import traceback

        traceback.print_exc()

        return f"""
        <h2>Error occurred</h2>
        <pre>{traceback.format_exc()}</pre>
        """



# ==========================
# Run Application
# ==========================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False
    )