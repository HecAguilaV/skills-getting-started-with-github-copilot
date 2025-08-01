"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    # Sports Activities
    "Basketball Team": {
        "description": "Competitive basketball training and inter-school tournaments",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["alex@mergington.edu", "sarah@mergington.edu"]
    },
    "Swimming Club": {
        "description": "Swimming techniques, endurance training, and water safety",
        "schedule": "Tuesdays and Thursdays, 7:00 AM - 8:30 AM",
        "max_participants": 25,
        "participants": ["marcus@mergington.edu", "lily@mergington.edu"]
    },
    # Artistic Activities
    "Drama Club": {
        "description": "Acting, script reading, and theatrical performances",
        "schedule": "Thursdays, 3:30 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["isabella@mergington.edu", "james@mergington.edu"]
    },
    "Art Studio": {
        "description": "Painting, drawing, sculpture, and mixed media projects",
        "schedule": "Fridays, 2:00 PM - 4:00 PM",
        "max_participants": 16,
        "participants": ["maya@mergington.edu", "ethan@mergington.edu"]
    },
    # Intellectual Activities
    "Debate Team": {
        "description": "Public speaking, argumentation skills, and competitive debates",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["ava@mergington.edu", "noah@mergington.edu"]
    },
    "Science Olympiad": {
        "description": "STEM competitions, experiments, and scientific problem-solving",
        "schedule": "Saturdays, 9:00 AM - 12:00 PM",
        "max_participants": 20,
        "participants": ["zoe@mergington.edu", "lucas@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")

# Validate student is not already signed up

def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
