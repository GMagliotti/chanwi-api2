import datetime
from models.models import Producer, Post
import daos.postDao as postDao
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from database.database import SessionLocal, engine
from datetime import datetime
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

@router.post("/produced/{producer_id}/posts", response_model=None)
def create_post(
    producer_id: int,
    title: str,
    description: str,
    price: float,
    tag: str,
    stock: int,
    start_time: datetime= datetime.now(),  
    end_time: Optional[datetime] = None,    
    db: Session = Depends(get_db)
):
    return postDao.create_post(
        producer_id=producer_id,
        title=title,
        description=description,
        price=price,
        tag=tag,
        stock=stock,
        start_time=start_time,
        end_time=end_time,
        db=db)

@router.get("/produced/{producer_id}/posts")
def get_posts_by_producer(producer_id: int, db: Session = Depends(get_db)):
    return postDao.get_posts_by_producer(producer_id=producer_id, db=db)
