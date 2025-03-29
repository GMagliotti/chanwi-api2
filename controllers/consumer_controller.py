from fastapi import APIRouter, Depends
from typing import Optional
from database.database import SessionLocal

from daos import consumerDao
from models.models import Consumer, ConsumerSchema
from sqlalchemy.orm import Session

router = APIRouter(prefix="/consumers", tags=["consumers"])

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/consumer", response_model=None)
def create(consumer: ConsumerSchema, db: Session):
    return consumerDao.create_consumer(consumer.email, consumer.password, consumer.name, consumer.surname)