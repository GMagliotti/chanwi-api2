from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema for creating a drive
class CreateDriveRequest(BaseModel):
    drive_id: int
    producer_id: int
    receiver_id: int
    start_time: datetime
    end_time: Optional[datetime] = None

# Schema for getting drives by receiver
class GetDrivesByReceiverRequest(BaseModel):
    receiver_id: int