# models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from database.database import Base
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class ProducerSchema(BaseModel):
    id: int = Field(default=None, title="Producer ID")
    email: EmailStr = Field(..., title="Email", description="Email of the producer")
    password: str = Field(..., title="Password", description="Password of the producer")
    business_name: str = Field(..., title="Business Name", description="Name of the producer's business")
    latitude: float = Field(..., title="Latitude", description="Latitude of the producer's location")
    longitude: float = Field(..., title="Longitude", description="Longitude of the producer's location")
    address: str = Field(..., title="Address", description="Address of the producer's location")
    description: str = Field(None, title="Description", description="Description of the producer's business")
    rating: float = Field(None, title="Rating", description="Rating of the producer's business")
    posts: list = Field(default=[], title="Posts", description="List of posts by the producer")

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
    rating = Column(Float,default=0)
    posts = relationship("Post", back_populates="producer")

class ReceiverSchema(BaseModel):
    id: int = Field(default=None, title="Receiver ID")
    email: EmailStr = Field(..., title="Email", description="Email of the receiver")
    password: str = Field(..., title="Password", description="Password of the receiver")
    organization_name: str = Field(..., title="Organization Name", description="Name of the receiver's organization")
    latitude: float = Field(..., title="Latitude", description="Latitude of the receiver's location")
    longitude: float = Field(..., title="Longitude", description="Longitude of the receiver's location")
    address: str = Field(..., title="Address", description="Address of the receiver's location")
    drives: list = Field(default=[], title="Drives", description="List of drives associated with the receiver")

class Receiver(Base):
    __tablename__="receivers"

    id=Column(Integer, primary_key=True,index=True,autoincrement=True)
    email=Column(String)
    password=Column(String)
    organization_name=Column(String)
    latitude=Column(Float)
    longitude=Column(Float)
    address=Column(String)


    drives = relationship("Drive", back_populates="receiver")

class ConsumerSchema(BaseModel):
    id: int = Field(default=None, title="Consumer ID")
    email: EmailStr = Field(..., title="Email", description="Email of the consumer")
    password: str = Field(..., title="Password", description="Password of the consumer")
    name: str = Field(..., title="Name", description="Name of the consumer")
    surname: str = Field(..., title="Surname", description="Surname of the consumer")
    orders: list = Field(default=[], title="Orders", description="List of orders made by the consumer")

class Consumer(Base):
    __tablename__ = "consumers"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    orders = relationship("Order", back_populates="consumer")

class DriveSchema(BaseModel):
    id: int = Field(default=None, title="Drive ID")
    title: str = Field(..., title="Title", description="Title of the drive")
    description: str = Field(None, title="Description", description="Description of the drive")
    start_time: datetime = Field(..., title="Start Time", description="Start time of the drive")
    end_time: datetime = Field(None, title="End Time", description="End time of the drive")
    receiver_id: int = Field(..., title="Receiver ID", description="ID of the receiver associated with the drive")
    receiver: ReceiverSchema = Field(None, title="Receiver", description="Receiver associated with the drive")

class Drive(Base):
    __tablename__ = "drives"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String(1024), nullable=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime)
    
    # Foreign key for Receiver
    receiver_id = Column(Integer, ForeignKey('receivers.id'), nullable=False)
    
    # Relationship to Receiver (one-to-many)
    receiver = relationship("Receiver", back_populates="drives")

class PostSchema(BaseModel):
    id: int = Field(default=None, title="Post ID")
    title: str = Field(..., title="Title", description="Title of the post")
    description: str = Field(None, title="Description", description="Description of the post")
    price: float = Field(..., title="Price", description="Price of the post")
    tag: str = Field(None, title="Tag", description="Tag associated with the post")
    stock: int = Field(..., title="Stock", description="Stock available for the post")
    start_time: datetime = Field(..., title="Start Time", description="Start time of the post")
    end_time: datetime = Field(None, title="End Time", description="End time of the post")
    producer_id: int = Field(..., title="Producer ID", description="ID of the producer associated with the post")
    producer: ProducerSchema = Field(None, title="Producer", description="Producer associated with the post")
    orders: list = Field(default=[], title="Orders", description="List of orders associated with the post")

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

class OrderSchema(BaseModel):
    id: int = Field(default=None, title="Order ID")
    quantity: int = Field(..., title="Quantity", description="Quantity of the order")
    received: bool = Field(default=False, title="Received", description="Whether the order has been received")
    consumer_id: int = Field(..., title="Consumer ID", description="ID of the consumer associated with the order")
    post_id: int = Field(..., title="Post ID", description="ID of the post associated with the order")
    consumer: ConsumerSchema = Field(None, title="Consumer", description="Consumer associated with the order")
    post: PostSchema = Field(None, title="Post", description="Post associated with the order")

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