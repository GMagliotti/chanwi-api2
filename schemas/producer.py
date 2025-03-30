from pydantic import BaseModel

class ProducerCreate(BaseModel): 
    email: str 
    password: str 
    business_name: str
    latitude: float
    longitude: float 
    address: str
    description: str 
    rating: float

class ProducerResponse(BaseModel): 
    email: str 
    id:int
    business_name: str
    latitude: float
    longitude: float 
    address: str
    description: str 
