from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import ConsumerController,receiverController, ProducerController, driveController, orderController, postController

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, PUT, DELETE, OPTIONS)
    allow_headers=["*"], # Allows all headers
)


app.include_router(ConsumerController.router, tags=["consumers"])
app.include_router(receiverController.router, tags=["receivers"])
app.include_router(ProducerController.router, tags=["producers"])
app.include_router(driveController.router, tags=["drives"])
app.include_router(orderController.router, tags=["orders"])
app.include_router(postController.router, tags=["posts"])