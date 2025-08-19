import fitz
from paddleocr import PaddleOCR
import sys
import os
ocr = PaddleOCR(use_angle_cls=True, lang='en')

def extract_text_from_scanned_pdf(pdf_path : str)-> str:
    doc = fitz.open(pdf_path)
    all_text = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        if text.strip():
            all_text.append("\n--- Page {page_num} ---\n{text}")
            continue

        pix = page.get_pixmap(dpi = 200)
        img_path = f"temp_page_{page_num}.png"
        pix.save(img_path)
        result = ocr.ocr(img_path, cls=True)
        page_text = " ".join([line[1][0] for line in result[0]]) if result[0] else ""
        all_text.append(f"\n--- Page {page_num} (OCR) ---\n{page_text}")
        os.remove(img_path)

    return "\n".join(all_text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/ocr_pdf.py <scanned.pdf>")
    else:
        pdf_file = sys.argv[1]
        print(extract_text_from_scanned_pdf(pdf_file)[:2000])
