# Install: python -m pip install pypdf
from pypdf import PdfReader

pdf_path = "sample.pdf"

# Hinglish: PdfReader PDF ko read karta hai. Har page par extract_text() use kar sakte ho.
try:
    reader = PdfReader(pdf_path)
    full_text = ""

    for page_no, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        print(f"--- Page {page_no} ---")
        print(text[:500])
        full_text += text + "\n"

    with open("extracted_pdf_text.txt", "w", encoding="utf-8") as file:
        file.write(full_text)
except FileNotFoundError:
    print("sample.pdf same folder me rakho.")

# Note: scanned/image PDF ke liye OCR chahiye hota hai.
