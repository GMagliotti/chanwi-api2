from typing import Union

from fastapi import FastAPI
from controllers import ConsumerController,receiverController, ProducerController, driveController, orderController, postController

app = FastAPI()
app.include_router(ConsumerController.router, tags=["consumers"])
app.include_router(receiverController.router, tags=["receivers"])
app.include_router(ProducerController.router, tags=["producers"])
app.include_router(driveController.router, tags=["drives"])
app.include_router(orderController.router, tags=["orders"])
app.include_router(postController.router, tags=["posts"])