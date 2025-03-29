from pydantic import BaseModel
from typing import Optional

# Schema for creating a receiver
class CreateReceiverRequest(BaseModel):
    email: str
    password: str
    organization_name: str
    latitude: float
    longitude: float
    address: str

# Schema for getting receivers by proximity
class GetReceiversByProximityRequest(BaseModel):
    user_latitude: float
    user_longitude: float