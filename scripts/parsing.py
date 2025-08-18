import fitz
import sys
def extract_pdf(pdf_path : str) -> str:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text() + "\n"
    return text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/parse_pdf.py <file.pdf>")
    else:
        pdf_file = sys.argv[1]
        print(extract_pdf(pdf_file)[:1000])

