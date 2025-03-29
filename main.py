from typing import Union

from fastapi import FastAPI
from controllers import ConsumerController,receiverController, ProducerController

app = FastAPI()
app.include_router(ConsumerController.router, tags=["consumers"])
app.include_router(receiverController.router, tags=["receivers"])
app.include_router(ProducerController.router, tags=["producers"])
