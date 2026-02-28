from fastapi import APIRouter, Depends

from core.dependencies import get_current_user

router = APIRouter(tags=["profile"])


@router.get("/profile")
async def get_profile(current_user = Depends(get_current_user)):
    return {
        "id": str(current_user["_id"]),
        "name": current_user["name"],
        "email": current_user["email"]
    }