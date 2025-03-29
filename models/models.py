# models.py
from sqlalchemy import Column, Integer, String, Float,DateTime, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from database.database import Base



class Producer(Base):
    __tablename__ = "producers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, index=True)
    password = Column(String)
    business_name = Column("business_name", String)
    latitude = Column(Float)
    longitude = Column(Float)
    address = Column(String)
    description = Column(String(length=1024))
    rating = Column(Float)
    posts = relationship("Post", back_populates="producer")

class Receiver(Base):
    __tablename__="receivers"

    id=Column(Integer, primary_key=True,index=True)
    email=Column(String)
    password=Column(String)
    organization_name=Column(String)
    latitude=Column(Float)
    longitude=Column(Float)
    address=Column(String)


    drives = relationship("Drive", back_populates="receiver")

class Consumer(Base):
    __tablename__ = "consumers"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    orders = relationship("Order", back_populates="consumer")

class Drive(Base):
    __tablename__ = "drives"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String(1024), nullable=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime)
    
    # Foreign key for Receiver
    receiver_id = Column(Integer, ForeignKey('receivers.id'), nullable=False)
    
    # Relationship to Receiver (one-to-many)
    receiver = relationship("Receiver", back_populates="drives")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String(1024), nullable=True)
    price = Column(Float, nullable=False)
    tag = Column(String, nullable=True)
    stock = Column(Integer, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, )
    
    # Foreign key for Producer
    producer_id = Column(Integer, ForeignKey('producers.id'), nullable=False)
    
    # Relationship to Producer (one-to-many)
    producer = relationship("Producer", back_populates="posts")
    # Relationship to Order (one-to-many)
    orders = relationship("Order", back_populates="post")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    received = Column(Boolean, default=False)

    # Foreign keys for Consumer and Post
    consumer_id = Column(Integer, ForeignKey('consumers.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    
    # Relationship to Consumer (many-to-one)
    consumer = relationship("Consumer", back_populates="orders")
    
    # Relationship to Post (many-to-one)
    post = relationship("Post", back_populates="orders")