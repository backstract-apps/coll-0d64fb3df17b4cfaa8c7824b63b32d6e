from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/school/')
async def get_school(db: Session = Depends(get_db)):
    try:
        return await service.get_school(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/school/school_id')
async def get_school_school_id(school_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_school_school_id(db, school_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/school/school_id/')
async def put_school_school_id(raw_data: schemas.PutSchoolSchoolId, db: Session = Depends(get_db)):
    try:
        return await service.put_school_school_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/school/school_id')
async def delete_school_school_id(school_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_school_school_id(db, school_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/')
async def get_students(db: Session = Depends(get_db)):
    try:
        return await service.get_students(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/student_id')
async def get_students_student_id(student_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_students_student_id(db, student_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/students/student_id/')
async def put_students_student_id(raw_data: schemas.PutStudentsStudentId, db: Session = Depends(get_db)):
    try:
        return await service.put_students_student_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/students/student_id')
async def delete_students_student_id(student_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_students_student_id(db, student_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/students/')
async def post_students(raw_data: schemas.PostStudents, db: Session = Depends(get_db)):
    try:
        return await service.post_students(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/school/')
async def post_school(raw_data: schemas.PostSchool, db: Session = Depends(get_db)):
    try:
        return await service.post_school(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/demo')
async def post_demo(raw_data: schemas.PostDemo, db: Session = Depends(get_db)):
    try:
        return await service.post_demo(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/records')
async def get_students_records(full_name: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.get_students_records(db, full_name)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/join1')
async def get_join1(db: Session = Depends(get_db)):
    try:
        return await service.get_join1(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

