from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="FastAPI uv Manager")

app.include_router(router)


@app.get("/")
async def root():
    return {
        "status": "online", 
        "environment": "devcontainer", 
        "message": "Welcome to the Task Manager API. Visit /docs for Swagger UI."
    }