# Student CRUD API

A simple REST API built using FastAPI to manage student records.

## Features
- Create a student
- View all students
- View a student by ID
- Update student details
- Delete a student
- Input validation using Pydantic

## Technologies Used
- Python
- FastAPI
- Pydantic
- Uvicorn

## Installation and Setup

1. Install the required packages:

   `pip install -r requirements.txt`

2. Run the application:

   `python -m uvicorn main:app --reload`

3. Open Swagger UI in your browser:

   `http://127.0.0.1:8000/docs`

## Note
This project uses in-memory storage and does not use a database. Student data resets when the server restarts.