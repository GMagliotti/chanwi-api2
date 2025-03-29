from sqlalchemy.orm import Session

from models.models import Consumer

def create_consumer(db: Session, email: str, password: str, name: str, surname: str) -> Consumer:
    db_consumer = Consumer(email=email, password=password, name=name, surname=surname)
    db.add(db_consumer)
    db.commit()
    db.refresh(db_consumer)
    return db_consumer
