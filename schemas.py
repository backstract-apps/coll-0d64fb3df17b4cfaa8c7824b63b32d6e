from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class School(BaseModel):
    school_name: str
    address: Optional[str]=None
    city: Optional[str]=None
    state: Optional[str]=None
    pincode: Optional[str]=None
    created_at: Optional[datetime.time]=None


class ReadSchool(BaseModel):
    school_name: str
    address: Optional[str]=None
    city: Optional[str]=None
    state: Optional[str]=None
    pincode: Optional[str]=None
    created_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class Students(BaseModel):
    full_name: str
    email: str
    age: Optional[int]=None
    grade: Optional[str]=None
    school_id: Optional[int]=None
    enrolled_at: Optional[datetime.time]=None


class ReadStudents(BaseModel):
    full_name: str
    email: str
    age: Optional[int]=None
    grade: Optional[str]=None
    school_id: Optional[int]=None
    enrolled_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True


class Teachers(BaseModel):
    full_name: Optional[str]=None
    email: Optional[str]=None
    subject: Optional[str]=None
    phone_numb0er: Optional[str]=None
    school_id: Optional[int]=None


class ReadTeachers(BaseModel):
    full_name: Optional[str]=None
    email: Optional[str]=None
    subject: Optional[str]=None
    phone_numb0er: Optional[str]=None
    school_id: Optional[int]=None
    class Config:
        from_attributes = True


class Classes(BaseModel):
    lass_name: Optional[str]=None
    section: Optional[str]=None
    grade_level: Optional[str]=None


class ReadClasses(BaseModel):
    lass_name: Optional[str]=None
    section: Optional[str]=None
    grade_level: Optional[str]=None
    class Config:
        from_attributes = True




class PutSchoolSchoolId(BaseModel):
    school_id: Optional[int]=None
    school_name: Optional[str]=None
    address: Optional[str]=None
    city: Optional[str]=None
    state: Optional[str]=None
    pincode: Optional[str]=None
    created_at: Optional[Any]=None

    class Config:
        from_attributes = True



class PutStudentsStudentId(BaseModel):
    student_id: Optional[int]=None
    full_name: Optional[str]=None
    email: Optional[str]=None
    age: Optional[int]=None
    grade: Optional[str]=None
    school_id: Optional[int]=None
    enrolled_at: Optional[Any]=None

    class Config:
        from_attributes = True



class PostStudents(BaseModel):
    student_id: Optional[int]=None
    full_name: Optional[str]=None
    email: Optional[str]=None
    age: Optional[int]=None
    grade: Optional[str]=None
    school_id: Optional[int]=None
    enrolled_at: Optional[str]=None

    class Config:
        from_attributes = True



class PostSchool(BaseModel):
    school_name: Optional[str]=None
    address: Optional[str]=None
    city: Optional[str]=None
    state: Optional[str]=None
    pincode: Optional[str]=None

    class Config:
        from_attributes = True



class PostDemo(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)

    class Config:
        from_attributes = True

