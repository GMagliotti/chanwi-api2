# main.py
from fastapi import APIRouter, FastAPI, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine
from models.models import Producer
from daos import producerDao as producerDao

# Create the database tables if not already created
Producer.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=None)
def create_producer(email: str, password: str, business_name: str,
                    latitude: float, longitude: float, address: str,
                    description: str, rating: float, db: Session = Depends(get_db)):
    return producerDao.create_producer(db, email, password, business_name, latitude, longitude, address, description, rating)

@router.get("")
def get_producers_by_proximity(user_latitude: float, user_longitude: float, db: Session = Depends(get_db)):
    return producerDao.get_producers_by_proximity(db, user_latitude, user_longitude)
