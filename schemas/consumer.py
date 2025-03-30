from pydantic import BaseModel

class ConsumerCreate(BaseModel):
    email: str
    password: str
    name: str
    surname: str
    
class ConsumerResponse(BaseModel):
    email: str
    name: str
    surname: str
    id:int