from sqlalchemy.orm import Session
from models.models import Order,Post  # Assuming you have an Order SQLAlchemy model
from typing import List, Optional
import math

def create(quantity:int,received:bool,consumer_id:int,post_id:int, db: Session) -> Order:
    order = Order(
        quantity=quantity,
        received=received,
        consumer_id=consumer_id,
        post_id=post_id
    )
    db.add(order)
    db.commit()
    post=db.query(Post).filter(Post.id==post_id).first()
    post.stock-=min(post.stock,quantity)
    db.refresh(order)  # Refresh the instance to get the generated ID
    db.commit()
    return order
def get_orders_dao(post_id: Optional[int], consumer_id: Optional[int],incompleted_orders_only:bool, db: Session) -> List[Order]:
    """
    Retrieve orders filtered by post_id and/or consumer_id.
    """
    query = db.query(Order)
    if post_id is not None:
        query = query.filter(Order.post_id == post_id)
    if consumer_id is not None:
        query = query.filter(Order.consumer_id == consumer_id)
    if incompleted_orders_only:
       query= query.filter(Order.received==False)
    return query.all()
def complete_order_from_id(db:Session,order_id:int):
    order=db.query(Order).filter(Order.id==order_id).first()
    if order is None:
        return None
    order.received=True
    db.commit()
    return order
    