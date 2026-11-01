from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

applications = []


class JobApplication(BaseModel):
    company: str
    position: str
    location: str
    status: str


@app.get("/")
def home():
    return {"message": "Welcome to Job Application Tracker!"}

# Προσθήκη αίτησης

@app.post("/applications")
def create_application(application: JobApplication):
    applications.append(application.model_dump())

    return {
        "message": "Application created successfully!",
        "application": application
    }

#Εμφάνιση αιτήσεων

@app.get("/applications")
def get_applications():
    return applications