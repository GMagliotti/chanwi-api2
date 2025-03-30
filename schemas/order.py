from pydantic import BaseModel
from typing import Optional

# Schema for creating an order
class CreateOrderRequest(BaseModel):
    quantity: int
    consumer_id: int
    post_id: int
    received: bool

# Schema for getting orders
class GetOrdersRequest(BaseModel):
    post_id: Optional[int] = None
    consumer_id: Optional[int] = None
class Order(BaseModel):
    id: int
    quantity: int
    consumer_id: int
    post_id: int
    received: bool

    class Config:
        orm_mode = True