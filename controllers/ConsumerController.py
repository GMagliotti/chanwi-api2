from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from models.models import Consumer
from daos.ConsumerDao import ConsumerDAO

router = APIRouter(prefix="/consumers", tags=["consumers"])

@router.post("/", response_model=Consumer)
def create_consumer(consumer: Consumer, db: Session = Depends(get_db)):
    dao = ConsumerDAO(db)
    return dao.create(consumer)