from fastapi import APIRouter, Depends, HTTPException
from schemas.userCredentials import UserCredentials
from sqlalchemy.orm import Session
from database.database import SessionLocal
from models.models import Receiver, Producer, Consumer

router = APIRouter(prefix='login', tags=["Login"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def login(credentials: UserCredentials, db: Session = Depends(get_db)):
    roleMap = { "receiver": Receiver, "producer": Producer, "consumer": Consumer }
    role = roleMap.get(credentials.role)
    if not role:
        raise HTTPException(status_code=400, detail="Invalid role")
    # Assuming you have a function to verify username and password
    user = db.query(role).filter(role.username == credentials.username, role.password == credentials.password).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": user.id}