from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "name": "John",
        "age": 17,
        "year": "year 12"
    }
}

class Student(BaseModel):
    Name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    Name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get('/')
def index():
    return {"name": "First Dat"}

@app.get("/get-students/{student_id}")
def get_students(student_id: int = Path(..., description="The ID of the student you want to view", gt=0)):
    return students[student_id]

@app.get("/get-by-name")
def get_by_name(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id : int, student : Student):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    students[student_id] = student
    if student.name != None:
        student[student_id].name = student.name
    return students[student_id]