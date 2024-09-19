from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    student_id: str = Field(...)
    student_name: str = Field(...)
    student_mail: EmailStr = Field(...)
    student_branch: str = Field(...)
    student_grades: float = Field(..., ge=0.0, le=10.0)

class UpdateStudentModel(BaseModel):
    student_name: Optional[str]
    student_mail: Optional[EmailStr]
    student_branch: Optional[str]
    student_grades: Optional[float]
