from schemas.producer import ProducerCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from models.models import Producer
from daos.ProducerDao import ProducerDAO

router = APIRouter(prefix = "/producers", tags=["producers"])

@router.post("/", response_model=ProducerCreate)
def CreateProducer(producer_data: ProducerCreate, db: Session = Depends(get_db)):
    dao = ProducerDAO(db)
    producer = Producer(**producer_data.model_dump())
    return dao.create(producer)


@router.get("/")
def get_producers_by_proximity(user_latitude: float, user_longitude: float, db: Session = Depends(get_db)):
    dao = ProducerDAO(db)
    return dao.get_by_proximity(user_latitude, user_longitude)