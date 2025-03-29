from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from daos.orderDao import create, get_orders
from database.database import SessionLocal
from schemas.order import CreateOrderRequest, GetOrdersRequest,Order

router = APIRouter(prefix="/orders", tags=["orders"])

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=None)
def create_order(request: CreateOrderRequest, db: Session = Depends(get_db)):
    return create(
        id=request.order_id,
        quantity=request.quantity,
        received=request.received,
        consumer_id=request.consumer_id,
        post_id=request.post_id,
        db=db
    )

@router.get("/", response_model=List[Order])
def get_orders(post_id:int,consumer_id:int, db: Session = Depends(get_db)):
    return get_orders(
        post_id=post_id,
        consumer_id=consumer_id,
        db=db
    )