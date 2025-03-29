from fastapi import APIRouter, FastAPI, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine
from models.models import Producer
from daos import receiverDao
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

@router.post("",response_model=None)
def create_receiver(email: str, password: str, organization_name:str, latitude: float, longitude: float, address: str,db= Depends(get_db)):
    return receiverDao.create_receiver(db=db,email=email, password=password, organization_name=organization_name, latitude=latitude, longitude=longitude, address=address)
@router.get("")
def get_receivers_by_proximity(user_latitude: float, user_longitude: float, db: Session = Depends(get_db)):
    return receiverDao.get_receivers_by_proximity(db, user_latitude, user_longitude)