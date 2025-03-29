from sqlalchemy.orm import Session
from models.models import Order,Post  # Assuming you have an Order SQLAlchemy model
from typing import List, Optional
import math

def create( id:int,quantity:int,received:int,consumer_id:int,post_id:int, db: Session) -> Order:
    order = Order(
        id=id,
        quantity=quantity,
        received=received,
        consumer_id=consumer_id,
        post_id=post_id
    )
    db.add(order)
    db.commit()
    post=db.query(Post).filter(Post.id==id).first()
    post.stock-=math.min(post.stock,quantity)
    db.refresh(order)  # Refresh the instance to get the generated ID
    db.flush(post)
    return order
def get_orders(post_id: Optional[int], consumer_id: Optional[int], db: Session) -> List[Order]:
    """
    Retrieve orders filtered by post_id and/or consumer_id.
    """
    query = db.query(Order)
    if post_id is not None:
        query = query.filter(Order.post_id == post_id)
    if consumer_id is not None:
        query = query.filter(Order.consumer_id == consumer_id)
    return query.all()