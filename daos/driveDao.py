from sqlalchemy.orm import Session
import datetime as dt


from models.models import Drive, Receiver

def create_drive(db: Session, title: str, description: str, start_time: dt.datetime, end_time: dt.datetime, receiver_id:int) -> Drive:
    db_drive = Drive(title=title, description=description, start_time=start_time, end_time=end_time, receiver_id=receiver_id)
    db.add(db_drive)
    db.commit()
    db.refresh(db_drive)
    return db_drive

def get_drives_by_receiver(db: Session, receiver_id: int):
    return db.query(Drive)\
        .filter(Drive.receiver_id == receiver_id)\
        .all()