from models.models import Producer
import daos.postDao as postDao
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine
from schemas.post import CreatePostRequest, PostResponse
from typing import List

# Create the database tables if not already created
Producer.metadata.create_all(bind=engine)

router = APIRouter(tags=["posts"])

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/producer/{producer_id}/posts", response_model=PostResponse)
def create_post(producer_id: int, request: CreatePostRequest, db: Session = Depends(get_db)):
    return postDao.create_post(
        producer_id=producer_id,
        title=request.title,
        description=request.description,
        price=request.price,
        tag=request.tag,
        stock=request.stock,
        start_time=request.start_time,
        end_time=request.end_time,
        db=db
    )

@router.get("/producer/{producer_id}/posts", response_model=List[PostResponse])
def get_posts_by_producer(producer_id: int, db: Session = Depends(get_db)):
    return postDao.get_posts_by_producer(producer_id=producer_id, db=db)
