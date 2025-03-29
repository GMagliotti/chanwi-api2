# crud.py
from sqlalchemy.orm import Session
from models.models import Producer
from daos.geoUtils import calculate_distance

def create_producer(db: Session, email: str, password: str, business_name: str,
                    latitude: float, longitude: float, address: str,
                    description: str, rating: float):
    db_producer = Producer(email=email, password=password, business_name=business_name,
                           latitude=latitude, longitude=longitude, address=address,
                           description=description, rating=rating)
    breakpoint()
    db.add(db_producer)
    db.commit()
    db.refresh(db_producer)
    return db_producer

def get_producers_by_proximity(db: Session, user_latitude: float, user_longitude: float):
    # Assuming we already have a function to calculate the distance
    producers = db.query(Producer).all()
    nearby_producers = []

    for producer in producers:
        distance = calculate_distance(user_latitude, user_longitude, producer.latitude, producer.longitude)
        if distance <= 1000:  # 1000 meters or 1 km
            nearby_producers.append(producer)

    return nearby_producers


