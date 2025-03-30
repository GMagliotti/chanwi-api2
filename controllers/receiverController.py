from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine
from models.models import Producer
from daos import receiverDao
from schemas.receiver import CreateReceiverRequest,CreateReceiverResponse, GetReceiversByProximityRequest

# Create the database tables if not already created
Producer.metadata.create_all(bind=engine)

router = APIRouter(prefix="/receivers", tags=["receivers"])

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CreateReceiverResponse)
def create_receiver(request: CreateReceiverRequest, db: Session = Depends(get_db)):
    return receiverDao.create_receiver(
        db=db,
        email=request.email,
        password=request.password,
        organization_name=request.organization_name,
        latitude=request.latitude,
        longitude=request.longitude,
        address=request.address
    )

@router.get("/")
def get_receivers_by_proximity(user_latitude:float,user_longitude:float, db: Session = Depends(get_db)):
    return receiverDao.get_receivers_by_proximity(
        db=db,
        user_latitude=user_latitude,
        user_longitude=user_longitude
    )
@router.get("/{receiver_id}",response_model=CreateReceiverResponse)
def find_receiver_by_id(receiver_id:int,db:Session=Depends(get_db)):
    receiver=receiverDao.find_receiver_by_id(db=db,receiver_id=receiver_id)
    if receiver is None:
        raise HTTPException(status_code=404,detail="Receiver not found")
    return receiver