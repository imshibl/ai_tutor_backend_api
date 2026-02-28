from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from routes.auth_routes import router as profile_router
app = FastAPI()

app.include_router(auth_router)

app.include_router(profile_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}