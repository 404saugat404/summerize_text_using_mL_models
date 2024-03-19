import pdfplumber
import json

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def save_text_to_json(text, json_path):
    with open(json_path, "w") as json_file:
        json.dump({"text": text}, json_file, indent=4)

# Replace "your_pdf_file.pdf" with the path to your PDF file
pdf_text = extract_text_from_pdf("/home/saugat/Desktop/summerizer_project/hello.pdf")

# Replace "output.json" with the desired path for your JSON file
save_text_to_json(pdf_text, "output.json")
