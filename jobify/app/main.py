from fastapi import FastAPI
from app.routes import user, auth, job, application
from app.database import Base, engine
from app.models import user as user_model  
from app.routes import profile

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Jobify Backend")

# Register routes
app.include_router(user.router, prefix="/api/users", tags=["Users"])
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(job.router, prefix="/api/jobs", tags=["Jobs"])
app.include_router(application.router, prefix="/api/applications", tags=["Applications"])
app.include_router(profile.router, prefix="/profile", tags=["Profile"])

@app.get("/")
def home():
    return {"message": "Welcome to Jobify!"}
