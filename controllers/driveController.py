# main.py
from fastapi import APIRouter, FastAPI, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine
from models.models import Drive
from daos import driveDao

# Create the database tables if not already created
Drive.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_drive(
    drive_id: int,
    producer_id: int,
    receiver_id: int,
    start_time: str,
    end_time: str,
    db: Session
):
    return driveDao.create_drive(drive_id, producer_id, receiver_id, start_time, end_time, db)

def get_drives_by_receiver(receiver_id: int, db: Session):
    return driveDao.get_drives_by_receiver(receiver_id, db)