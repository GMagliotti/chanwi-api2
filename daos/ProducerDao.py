from sqlalchemy.orm import Session
from sqlalchemy.future import select
from fastapi import Depends
from database.database import get_db
from models.models import Producer,Post
import daos.geoUtils as GeoUtils
from sqlalchemy import func

class ProducerDAO:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, producer: Producer) -> Producer:
        self.db.add(producer)
        self.db.commit()
        self.db.refresh(producer)
        return producer

    def get_all(self) -> list[Producer]:
        consumers = self.db.execute(select(Producer)).scalars().all()
        return consumers
    
    def get_by_proximity(self, latitude: float, longitude: float, max_distance_in_meters: int = 10000) -> list[Producer]:
        if latitude is None or longitude is None:
            return self.get_all()
        producers = self.db.query(Producer).join(Post, Producer.id == Post.producer_id).group_by(Producer.id).having(func.count(Post.id) >= 1).all()
        nearby_producers = []

        for producer in producers:
            distance = GeoUtils.calculate_distance(latitude, longitude, producer.latitude, producer.longitude);
            if distance <= max_distance_in_meters:
                nearby_producers.append(producer)
            
        return nearby_producers
    
    def get_all_producers(self,with_posts:bool):
        if with_posts:
            result = (
                self.db.query(Producer)
                .join(Post, Producer.id == Post.producer_id)
                .group_by(Producer.id)
                .having(func.count(Post.id) >= 1) 
                .all())
        else:
            result = self.db.query(Producer).all()
        return result
    def find_by_id(self,producer_id:int):
        return self.db.query(Producer).filter(Producer.id==producer_id).first()