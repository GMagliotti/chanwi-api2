from schemas.producer import ProducerCreate,ProducerResponse
from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.models import Producer
from daos.ProducerDao import ProducerDAO

router = APIRouter(prefix = "/producers", tags=["producers"])

@router.post("/", response_model=ProducerResponse)
def CreateProducer(producer_data: ProducerCreate, db: Session = Depends(get_db)):
    dao = ProducerDAO(db)
    producer = Producer(**producer_data.model_dump())
    return dao.create(producer)

@router.get("/posts")
def get_all_producers(with_posts:bool=False,db:Session=Depends(get_db)):
    dao=ProducerDAO(db)
    return dao.get_all_producers(with_posts=with_posts)
    

@router.get("/")
def get_producers_by_proximity(user_latitude: float, user_longitude: float, db: Session = Depends(get_db)):
    dao = ProducerDAO(db)
    return dao.get_by_proximity(user_latitude, user_longitude)

@router.get("/{producer_id}")
def find_producer(producer_id:int,db:Session=Depends(get_db)):
    dao=ProducerDAO(db)
    producer=dao.find_by_id(producer_id)
    if not producer:
        raise HTTPException(status_code=404,detail="Producer not found")
    return producer