from models.models import Post

def create_post(producer_id:int , title: str, description: str, price: float, tag: str, stock: int, start_time: datetime.datetime, db: Session):
    db_post=Post(producer_id=producerId,title=title,description=description,price=price,tag=tag,stock=stock,start_time=start_time)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
def get_posts_by_producer(producerId:int, db: Session):
    posts = db.query(Post).filter(Post.producer_id == producerId).all()
    return posts