# pdf_extractor.py
# Simple PDF → Text extractor tool

from pathlib import Path
import PyPDF2


def extract_text_from_pdf(pdf_path):
    """Read a PDF file and return all extracted text as a string."""
    pdf_path = Path(pdf_path)

    # Check if file exists
    if not pdf_path.exists():
        print(f"File not found: {pdf_path}")
        return ""

    # Open PDF in binary mode
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""

        # Loop through all pages
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n\n"

    return text


if __name__ == "__main__":
    # 1. Input PDF file name
    pdf_file = "sample.pdf"  # Change this name if your file is different

    # 2. Extract text
    extracted_text = extract_text_from_pdf(pdf_file)

    # 3. Save to a text file
    output_file = "extracted_output.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    print(f"Done! Extracted text saved to: {output_file}")
