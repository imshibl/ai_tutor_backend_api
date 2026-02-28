from fastapi import FastAPI
from routes.auth_routes import router as auth_router
from routes.profile_routes import router as profile_router
from routes.ai_routes import router as ai_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(ai_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}