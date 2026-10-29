
from fastapi import FastAPI
from routes.student_routes import router as student_router

app = FastAPI(
    title="University Student CRUD API",
    description="Student management using in-memory storage",
    version="1.0.0"
)

app.include_router(student_router)


@app.get("/")
def home():
    return {"message": "Student CRUD API is running"}
