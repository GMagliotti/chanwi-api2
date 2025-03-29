from pydantic import BaseModel
from typing import Optional

class ReceiverBase(BaseModel):
    latitude: float
    longitude: float
    name: str
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    # Include all other fields that should be editable via API

class ReceiverCreate(ReceiverBase):
    pass

class Receiver(ReceiverBase):
    id: int

    class Config:
        orm_mode = True