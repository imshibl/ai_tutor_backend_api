from fastapi import HTTPException
from pypdf import PdfReader
from io import BytesIO


async def extract_pdf_text(file):
    try:
        # Read uploaded file into memory
        contents = await file.read()

        # Reject empty file
        if not contents:
            raise HTTPException(status_code=400, detail="Invalid file")

        # Load PDF
        pdf = PdfReader(BytesIO(contents))

        # Reject empty PDFs
        if len(pdf.pages) == 0:
            raise HTTPException(status_code=400, detail="Invalid file")

        # Reject PDFs with more than 2 pages
        # if len(pdf.pages) > 2:
        #     raise HTTPException(status_code=400, detail="PDF > 2 pages")

        # Extract text from all pages
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        # Reject PDFs with no extractable text
        if not text.strip():
            raise HTTPException(status_code=400, detail="No text found")

        return text

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid file")