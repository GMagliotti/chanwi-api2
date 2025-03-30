from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select

from models.models import Receiver
from database.schema import ReceiverCreate
from fastapi import Depends
import math
from daos.geoUtils import calculate_distance


def create_receiver(db: Session,email: str, password: str, organization_name:str, latitude: float, longitude: float, address: str):
    db_receiver = Receiver(email=email, password=password, organization_name=organization_name, latitude=latitude, longitude=longitude, address=address)
    db.add(db_receiver)
    db.commit()
    db.refresh(db_receiver)
    return db_receiver

def get_receivers_by_proximity(db: Session, user_latitude: float, user_longitude: float, max_distance_in_meters: float = 10000) -> List[Receiver]:
    # Assuming we already have a function to calculate the distance
    receivers = db.query(Receiver).all()
    nearby_receivers = []

    for receiver in receivers:
        distance = calculate_distance(user_latitude, user_longitude, receiver.latitude, receiver.longitude)
        if distance <= max_distance_in_meters:  
            nearby_receivers.append(receiver)

    return nearby_receivers

def find_receiver_by_id(db:Session,receiver_id:int):
    return db.query(Receiver).filter(Receiver.id==receiver_id).first()