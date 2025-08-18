import docx
import sys

def extract_docx_text(docx_path: str) -> str:
    doc = docx.Document(docx_path)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/parse_docx.py <file.docx>")
    else:
        docx_file = sys.argv[1]
        print(extract_docx_text(docx_file)[:1000])