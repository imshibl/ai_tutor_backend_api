from motor.motor_asyncio import AsyncIOMotorClient
# add a dot if importing from the same file
from .config import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)

# client acts as a proxy to allow python to access mongo db database.
db = client["aitutor"]

# db is the variable for the database, db["user"/"notes"] are collections of the relevant data.
users_collection = db["users"]
notes_collection = db["notes"]