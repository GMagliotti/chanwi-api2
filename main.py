from typing import Union

from fastapi import FastAPI
from controllers import ConsumerController,receiverController

app = FastAPI()
app.include_router(ConsumerController.router, tags=["consumers"])
app.include_router(receiverController.router, tags=["receiver"])