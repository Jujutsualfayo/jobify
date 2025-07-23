# main.py

from fastapi import FastAPI
from app.routes import user
from app.database import Base, engine
from app.models import user as user_model  # This ensures the model is registered

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Jobify Backend")

# Include user routes
app.include_router(user.router, prefix="/api/users", tags=["Users"])

@app.get("/")
def home():
    return {"message": "Welcome to Jobify!"}


