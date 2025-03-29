from pydantic import BaseModel

class ConsumerCreate(BaseModel):
    email: str
    password: str
    name: str
    surname: str
