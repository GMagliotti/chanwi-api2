from models.models import Post
import datetime
import daos.postDao as postDao
from sqlalchemy.orm import Session

def create_post(producer_id:int , title: str, description: str, price: float, tag: str, stock: int, start_time: datetime,end_time:datetime ,db: Session):
    db_post=Post(producer_id=producer_id,title=title,description=description,price=price,tag=tag,stock=stock,start_time=start_time,end_time=end_time)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
def get_posts_by_producer(producer_id:int, db: Session):
    posts = db.query(Post).filter(Post.producer_id == producer_id).all()
    return posts