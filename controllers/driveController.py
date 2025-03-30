# main.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine
from models.models import Drive
from daos import driveDao
from schemas.drive import CreateDriveRequest, GetDrivesByReceiverRequest

# Create the database tables if not already created
Drive.metadata.create_all(bind=engine)

router = APIRouter(tags=["drives"])

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/receivers/{receiver_id}/drives", response_model=None)
def create_drive(request: CreateDriveRequest, db: Session = Depends(get_db)):
    return driveDao.create_drive(
        producer_id=request.producer_id,
        receiver_id=request.receiver_id,
        start_time=request.start_time,
        end_time=request.end_time,
        db=db
    )

@router.get("/receivers/{receiver_id}/drives")
def get_drives_by_receiver(receiver_id: int, db: Session=Depends(get_db)):
    return driveDao.get_drives_by_receiver(receiver_id, db)