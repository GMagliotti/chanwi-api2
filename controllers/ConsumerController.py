from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from models.models import Consumer
from schemas.consumer import ConsumerCreate
from daos.ConsumerDao import ConsumerDAO

router = APIRouter(prefix="/consumers", tags=["consumers"])

@router.post("/", response_model=ConsumerCreate)
def create_consumer(consumer_data: ConsumerCreate, db: Session = Depends(get_db)):
    dao = ConsumerDAO(db)
    consumer = Consumer(**consumer_data.model_dump())
    return dao.create(consumer)