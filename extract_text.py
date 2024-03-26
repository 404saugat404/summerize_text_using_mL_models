import fitz  # PyMuPDF
import json

def extract_text_from_pdf(pdf_path):
    try:
        with fitz.open(pdf_path) as pdf_document:
            text = ""
            for page_number in range(pdf_document.page_count):
                page = pdf_document[page_number]
                text += page.get_text()
            return text
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_text_to_json(text, json_path):
    try:
        with open(json_path, 'w') as json_file:
            json.dump({"text": text}, json_file, indent=4)
        print(f"Text saved to {json_path}")
    except Exception as e:
        print(f"Error saving to JSON: {e}")

# Prompt user for PDF file input
pdf_path = input("Enter the path to the PDF file: ")

# Check if the file exists
try:
    with open(pdf_path):
        pass
except FileNotFoundError:
    print(f"Error: The file '{pdf_path}' does not exist.")
    exit()

# Set the output JSON file path
json_path = "output.json"  # Replace with the desired output JSON file path

# Extract text from the PDF and save to JSON
extracted_text = extract_text_from_pdf(pdf_path)

if extracted_text:
    save_text_to_json(extracted_text, json_path)
else:
    print("Failed to extract text from the PDF.")
