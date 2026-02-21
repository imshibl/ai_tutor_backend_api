from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any

from jose import jwt, JWTError, ExpiredSignatureError
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHash

from .config import SECRET_KEY

# JWT settings
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 7

# Argon2 password hasher
ph = PasswordHasher()


def hash_password(password: str) -> str:
    """Hash a plain password using Argon2."""
    return ph.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against an Argon2 hash."""
    try:
        return ph.verify(hashed_password, plain_password)
    except (VerifyMismatchError, InvalidHash):
        return False


def create_access_token(name: str, email: str) -> str:
    """
    Create a JWT access token with:
    - name
    - email
    - exp (7 days)
    """
    expire = datetime.now(timezone.utc) + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)

    payload = {
        "name": name,
        "email": email,
        "exp": expire,
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def decode_token(token: str) -> Optional[Dict[str, Any]]:
    """
    Decode and validate JWT token.
    Returns payload if valid, otherwise None.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Make sure expected fields exist
        if "name" not in payload or "email" not in payload:
            return None

        return payload

    except ExpiredSignatureError:
        return None
    except JWTError:
        return None