from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from bson import ObjectId

from core.db import db, users_collection
from core.security import decode_token

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    # Token missing
    if not credentials:
        raise HTTPException(status_code=401, detail="Token missing")

    # Get token string
    token = credentials.credentials

    # Decode token
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token invalid or expired")

    # user_id missing
    email = payload.get("email")
    if not email:
        raise HTTPException(status_code=401, detail="email missing")

    # User not found in database
    existing_user = await users_collection.find_one({"email": email})
    if not existing_user:
        raise HTTPException(status_code=400, detail="Not found in database")
    
    # Return user data
    return existing_user