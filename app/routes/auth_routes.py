from fastapi import APIRouter, HTTPException

from models.auth_models import UserSignup, UserLogin
from core.security import hash_password, verify_password, create_access_token
from core import db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup")
async def signup(user: UserSignup):
    # Check if email already exists
    existing_user = await db.users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash password
    hashed_pw = hash_password(user.password)

    # Save user to MongoDB
    new_user = {
        "name": user.name,
        "email": user.email,
        "password": hashed_pw
    }
    result = await db.users_collection.insert_one(new_user)

    # Generate JWT token
    token = create_access_token(
        name=user.name,
        email=user.email
    )

    return {
        "message": "User created successfully",
        "access_token": token,
        "token_type": "bearer"
    }


@router.post("/login")
async def login(user: UserLogin):
    # Check if user exists
    existing_user = await db.users_collection.find_one({"email": user.email})
    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Verify password
    if not verify_password(user.password, existing_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Generate JWT token
    token = create_access_token(
        name=existing_user["name"],
        email=existing_user["email"]
    )

    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer"
    }