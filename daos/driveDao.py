from sqlalchemy.orm import Session
import datetime as dt


from models.models import Drive, Receiver

def create_drive(db: Session, title: str, description: str, startTime: dt, endTime: dt, receiver: Receiver) -> Drive:
    db_drive = Drive(title=title, description=description, startTime=startTime, endTime=endTime, receiver=receiver)
    db.add(db_drive)
    db.commit()
    db.refresh(db_drive)
    return db_drive

def get_drives_by_receiver(db: Session, receiver_id: int):
    return db.query(Drive)\
        .filter(Drive.receiver_id == receiver_id)\
        .all()