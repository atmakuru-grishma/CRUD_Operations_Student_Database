from fastapi import APIRouter, HTTPException
from app.models import Student, UpdateStudentModel
from app.database import student_collection
from bson import ObjectId

router = APIRouter()

@router.post("/student/", response_description="Add new student")
async def create_student(student: Student):
    student = student.dict()
    result = await student_collection.insert_one(student)
    return {"id": str(result.inserted_id)}

@router.get("/student/{id}", response_description="Get a single student")
async def read_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/student/{id}", response_description="Update a student")
async def update_student(id: str, student: UpdateStudentModel):
    student = {k: v for k, v in student.dict().items() if v is not None}
    if len(student) >= 1:
        update_result = await student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": student}
        )
        if update_result.modified_count == 1:
            updated_student = await student_collection.find_one({"_id": ObjectId(id)})
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found")

@router.delete("/student/{id}", response_description="Delete a student")
async def delete_student(id: str):
    delete_result = await student_collection.delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")
