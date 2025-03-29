from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine
from models.models import Producer
from daos import receiverDao
from schemas.receiver import CreateReceiverRequest, GetReceiversByProximityRequest

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

@router.post("/receivers", response_model=CreateReceiverRequest)
def create_receiver(request: CreateReceiverRequest, db: Session = Depends(get_db)):
    return receiverDao.create_receiver(
        db=db,
        email=request.email,
        password=request.password,
        organization_name=request.organization_name,
        latitude=request.latitude,
        longitude=request.longitude,
        address=request.address
    )

@router.get("/receivers")
def get_receivers_by_proximity(request: GetReceiversByProximityRequest, db: Session = Depends(get_db)):
    return receiverDao.get_receivers_by_proximity(
        db=db,
        user_latitude=request.user_latitude,
        user_longitude=request.user_longitude
    )