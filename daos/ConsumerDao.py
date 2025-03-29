from sqlalchemy.orm import Session
from sqlalchemy.future import select
from fastapi import Depends
from database.database import get_db
from models.models import Consumer

class ConsumerDAO:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, consumer: Consumer) -> Consumer:
        self.db.add(consumer)
        self.db.commit()
        self.db.refresh(consumer)
        return consumer