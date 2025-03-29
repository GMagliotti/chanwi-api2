from typing import List, Optional
from pydantic import BaseModel

class OrderBase(BaseModel):
    # Define order fields here if needed
    pass

class OrderResponse(OrderBase):
    id: int
    
    class Config:
        orm_mode = True

class ConsumerBase(BaseModel):
    email: str
    name: str
    surname: str

class ConsumerCreate(ConsumerBase):
    password: str

class ConsumerResponse(ConsumerBase):
    id: int
    orders: List[OrderResponse] = []
    
    class Config:
        orm_mode = True