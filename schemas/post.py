from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema for creating a post
class CreatePostRequest(BaseModel):
    title: str
    description: str
    price: float
    tag: str
    stock: int
    start_time: Optional[datetime] = datetime.now()
    end_time: Optional[datetime] = None

# Schema for the Post response
class PostResponse(BaseModel):
    id: int
    producer_id: int
    title: str
    description: str
    price: float
    tag: str
    stock: int
    start_time: datetime
    end_time: Optional[datetime]

    class Config:
        orm_mode = True