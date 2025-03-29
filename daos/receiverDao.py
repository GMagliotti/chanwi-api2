from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import Base, get_db
from models import Receiver
from database.schema import ReceiverCreate
from fastapi import Depends
import math

class ReceiverDao:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db  # This is equivalent to EntityManager in JPA

    def create(self, receiver: ReceiverCreate) -> Receiver:
        db_receiver = Receiver(**receiver.dict())
        self.db.add(db_receiver)
        self.db.commit()
        self.db.refresh(db_receiver)
        return db_receiver

    def find_by_proximity(self, user_latitude: float = None, user_longitude: float = None) -> List[Receiver]:
        if user_latitude is None or user_longitude is None:
            return self.find_all()
        
        receivers = self.find_all()
        nearby_receivers = []
        
        for receiver in receivers:
            distance = self._calculate_distance(
                user_latitude, user_longitude,
                receiver.latitude, receiver.longitude
            )
            
            if distance <= 1000:  # 1000 meters
                nearby_receivers.append(receiver)
        
        return nearby_receivers

    def find_all(self) -> List[Receiver]:
        return self.db.execute(select(Receiver)).scalars().all()

def _calculate_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    # Haversine formula implementation
    R = 6371000  # Earth radius in meters
    φ1 = math.radians(lat1)
    φ2 = math.radians(lat2)
    Δφ = math.radians(lat2 - lat1)
    Δλ = math.radians(lon2 - lon1)
    a = math.sin(Δφ/2) * math.sin(Δφ/2) + \
        math.cos(φ1) * math.cos(φ2) * \
        math.sin(Δλ/2) * math.sin(Δλ/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c