from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user, auth, job, application, education, experience, skill as skills
from app.database import Base, engine
from app.models import user as user_model  
from app.routes import profile
from app.routes import auth
from fastapi.staticfiles import StaticFiles

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Jobify Backend")

# ✅ Add CORS middleware (adjust allowed origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with frontend URL in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(user.router, prefix="/api/users", tags=["Users"])
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(job.router, prefix="/api/jobs", tags=["Jobs"])
app.include_router(application.router, prefix="/api/applications", tags=["Applications"])
app.include_router(profile.router, prefix="/profile", tags=["Profile"])
app.include_router(education.router, prefix="/education", tags=["Education"])
app.include_router(experience.router, prefix="/experience", tags=["Experience"])
app.include_router(skills.router)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return {"message": "Welcome to Jobify!"}
