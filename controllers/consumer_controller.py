from fastapi import APIRouter, Depends
from typing import Optional
from database.database import SessionLocal

from daos.consumerDao import ConsumerDao
from models.models import Consumer

router = APIRouter(prefix="/consumers", tags=["consumers"])

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=Consumer)
def create(self, consumer: Consumer):
    return self.consumer_dao.create(consumer)