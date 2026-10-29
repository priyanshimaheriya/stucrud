
from fastapi import APIRouter, Response, status
from models.student_model import Student, StudentCreate
from controllers import student_controller as controller

router = APIRouter()


# 1. Create Student
@router.post(
    "/students",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def create_student(data: StudentCreate):
    return controller.create_student(data)


# 2. Read All Students
@router.get("/students", response_model=list[Student])
def get_all_students():
    return controller.get_all_students()


# 3. Read Student by ID
@router.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    return controller.get_student_by_id(student_id)


# 4. Update Student
@router.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, data: StudentCreate):
    return controller.update_student(student_id, data)


# 5. Delete Student
@router.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(student_id: int):
    controller.delete_student(student_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
