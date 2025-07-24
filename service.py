from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_school(db: Session):

    query = db.query(models.School)

    school_all = query.all()
    school_all = (
        [new_data.to_dict() for new_data in school_all] if school_all else school_all
    )
    res = {
        "school_all": school_all,
    }
    return res


async def get_school_school_id(db: Session, school_id: int):

    query = db.query(models.School)
    query = query.filter(and_(models.School.school_id == school_id))

    school_one = query.first()

    school_one = (
        (school_one.to_dict() if hasattr(school_one, "to_dict") else vars(school_one))
        if school_one
        else school_one
    )

    res = {
        "school_one": school_one,
    }
    return res


async def put_school_school_id(db: Session, raw_data: schemas.PutSchoolSchoolId):
    school_id: int = raw_data.school_id
    school_name: str = raw_data.school_name
    address: str = raw_data.address
    city: str = raw_data.city
    state: str = raw_data.state
    pincode: str = raw_data.pincode
    created_at: datetime.datetime = raw_data.created_at

    query = db.query(models.School)
    query = query.filter(and_(models.School.school_id == school_id))
    school_edited_record = query.first()

    if school_edited_record:
        for key, value in {
            "city": city,
            "state": state,
            "address": address,
            "pincode": pincode,
            "school_id": school_id,
            "created_at": created_at,
            "school_name": school_name,
        }.items():
            setattr(school_edited_record, key, value)

        db.commit()
        db.refresh(school_edited_record)

        school_edited_record = (
            school_edited_record.to_dict()
            if hasattr(school_edited_record, "to_dict")
            else vars(school_edited_record)
        )
    res = {
        "school_edited_record": school_edited_record,
    }
    return res


async def delete_school_school_id(db: Session, school_id: int):

    query = db.query(models.School)
    query = query.filter(and_(models.School.school_id == school_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        school_deleted = record_to_delete.to_dict()
    else:
        school_deleted = record_to_delete
    res = {
        "school_deleted": school_deleted,
    }
    return res


async def get_students(db: Session):

    query = db.query(models.Students)

    students_all = query.all()
    students_all = (
        [new_data.to_dict() for new_data in students_all]
        if students_all
        else students_all
    )
    res = {
        "students_all": students_all,
    }
    return res


async def get_students_student_id(db: Session, student_id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.student_id == student_id))

    students_one = query.first()

    students_one = (
        (
            students_one.to_dict()
            if hasattr(students_one, "to_dict")
            else vars(students_one)
        )
        if students_one
        else students_one
    )

    res = {
        "students_one": students_one,
    }
    return res


async def put_students_student_id(db: Session, raw_data: schemas.PutStudentsStudentId):
    student_id: int = raw_data.student_id
    full_name: str = raw_data.full_name
    email: str = raw_data.email
    age: int = raw_data.age
    grade: str = raw_data.grade
    school_id: int = raw_data.school_id
    enrolled_at: datetime.datetime = raw_data.enrolled_at

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.student_id == student_id))
    students_edited_record = query.first()

    if students_edited_record:
        for key, value in {
            "age": age,
            "email": email,
            "grade": grade,
            "full_name": full_name,
            "school_id": school_id,
            "student_id": student_id,
            "enrolled_at": enrolled_at,
        }.items():
            setattr(students_edited_record, key, value)

        db.commit()
        db.refresh(students_edited_record)

        students_edited_record = (
            students_edited_record.to_dict()
            if hasattr(students_edited_record, "to_dict")
            else vars(students_edited_record)
        )
    res = {
        "students_edited_record": students_edited_record,
    }
    return res


async def delete_students_student_id(db: Session, student_id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.student_id == student_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        students_deleted = record_to_delete.to_dict()
    else:
        students_deleted = record_to_delete
    res = {
        "students_deleted": students_deleted,
    }
    return res


async def post_students(db: Session, raw_data: schemas.PostStudents):
    student_id: int = raw_data.student_id
    full_name: str = raw_data.full_name
    email: str = raw_data.email
    age: int = raw_data.age
    grade: str = raw_data.grade
    school_id: int = raw_data.school_id
    enrolled_at: str = raw_data.enrolled_at

    record_to_be_added = {
        "age": age,
        "email": email,
        "grade": grade,
        "full_name": full_name,
        "school_id": school_id,
        "student_id": student_id,
        "enrolled_at": enrolled_at,
    }
    new_students = models.Students(**record_to_be_added)
    db.add(new_students)
    db.commit()
    db.refresh(new_students)
    students_inserted_record = new_students.to_dict()

    res = {
        "students_inserted_record": students_inserted_record,
    }
    return res


async def post_school(db: Session, raw_data: schemas.PostSchool):
    school_name: str = raw_data.school_name
    address: str = raw_data.address
    city: str = raw_data.city
    state: str = raw_data.state
    pincode: str = raw_data.pincode

    record_to_be_added = {
        "city": city,
        "state": state,
        "address": address,
        "pincode": pincode,
        "school_name": school_name,
    }
    new_school = models.School(**record_to_be_added)
    db.add(new_school)
    db.commit()
    db.refresh(new_school)
    add_a_records1 = new_school.to_dict()

    res = {
        "add_a_records1": add_a_records1,
    }
    return res


async def post_demo(db: Session, raw_data: schemas.PostDemo):
    id: int = raw_data.id
    name: str = raw_data.name

    res = {}
    return res


async def get_students_records(db: Session, full_name: str):

    s = aliased(models.Students)
    query = db.query(models.Students, s)

    query = query.join(s, and_(models.Students.full_name == s.full_name))

    students_records = query.all()
    students_records = (
        [
            {
                "students_records_1": (
                    s1.to_dict() if hasattr(s1, "to_dict") else s1.__dict__
                ),
                "students_records_2": (
                    s2.to_dict() if hasattr(s2, "to_dict") else s2.__dict__
                ),
            }
            for s1, s2 in students_records
        ]
        if students_records
        else students_records
    )
    res = {
        "students_records": students_records,
    }
    return res


async def get_join1(db: Session):

    t = aliased(models.Teachers)
    query = db.query(models.Teachers, t)

    query = query.join(t, and_(models.Teachers.id == t.full_name))

    test = query.first()

    if test:
        s1, s2 = test
        test = {
            "test_1": s1.to_dict() if hasattr(s1, "to_dict") else vars(s1),
            "test_2": s2.to_dict() if hasattr(s2, "to_dict") else vars(s2),
        }

    res = {
        "teacher": test,
    }
    return res
