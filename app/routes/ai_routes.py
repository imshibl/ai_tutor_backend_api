from fastapi import APIRouter, UploadFile, File, HTTPException, Depends

from core.dependencies import get_current_user
from utils.pdf_utils import extract_pdf_text

router = APIRouter(tags=["pdf"])


@router.post("/pdf/upload")
async def upload_pdf(
    file: UploadFile = File(...),
    current_user = Depends(get_current_user)
):
    # Only allow PDF files
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    # Extract text from PDF
    text = await extract_pdf_text(file)

    return {
        "text": text
    }