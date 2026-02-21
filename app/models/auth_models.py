from pydantic import BaseModel, EmailStr, Field, field_validator


class UserSignup(BaseModel):
    # User's display name
    # min_length=2 ensures at least 2 characters are provided
    name: str = Field(..., min_length=2)

    # Validates email format automatically (e.g. user@example.com)
    email: EmailStr

    # Password field (we'll do custom validation below to prevent blank strings)
    password: str

class UserLogin(BaseModel):
    # Login requires a valid email format
    email: EmailStr

    # Password required for login
    password: str

