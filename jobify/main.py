# main.py

from fastapi import FastAPI
from app.routes import user

app = FastAPI(title="Jobify Backend")

# Include user routes
app.include_router(user.router, prefix="/api/users", tags=["Users"])

@app.get("/")
def home():
    return {"message": "Welcome to Jobify!"}

