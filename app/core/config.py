from dotenv import load_dotenv
import os


# Load variables from .env file
load_dotenv()

MONGO_URL = os.getenv("DB_URL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

# Optional: basic check so app fails early if missing
if not MONGO_URL:
    raise ValueError("MONGO_URL is not set in .env")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in .env")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in .env")