from fastapi import APIRouter, Depends,HTTPException
from typing import List
from sqlalchemy.orm import Session

from daos.orderDao import create, get_orders_dao, complete_order_from_id
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

@router.post("/", response_model=Order)
def create_order(request: CreateOrderRequest, db: Session = Depends(get_db)):
    return create(
        quantity=request.quantity,
        received=request.received,
        consumer_id=request.consumer_id,
        post_id=request.post_id,
        db=db
    )

@router.get("/", response_model=List[Order])
def get_orders(post_id:int,consumer_id:int, db: Session = Depends(get_db)):
    return get_orders_dao(
        post_id=post_id,
        consumer_id=consumer_id,
        db=db
    )
    
@router.post("/{order_id}")
def complete_order(order_id:int,db:Session=Depends(get_db)):
    order=complete_order_from_id(order_id=order_id,db=db)
    if order is None:
        raise HTTPException(status_code=404,detail="Order non existent")
    return order