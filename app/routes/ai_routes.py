from fastapi import APIRouter, UploadFile, File, HTTPException, Depends, Form
from core.dependencies import get_current_user
from utils.pdf_utils import extract_pdf_text

from ai.summarise_ai import generate_structured_summary

router = APIRouter(tags=["pdf"])


@router.post("/pdf/summarise")
async def summarise_pdf(
    text: str = Form(None),
    file: UploadFile = File(None),
    current_user = Depends(get_current_user)
):
    # Only allow PDF files
    if not text and not file:
        raise HTTPException(status_code=400, detail="Please input either text or pdf file")

    # Extract text from PDF if a file is uploaded otherwise just summarise input text
    
    if file:
        text = await extract_pdf_text(file)
    summary = generate_structured_summary(text)

    return {
        "summary": summary
    }