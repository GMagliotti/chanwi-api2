from typing import Union

from fastapi import FastAPI
from controllers import ConsumerController, ProducerController

app = FastAPI()
app.include_router(ConsumerController.router, tags=["consumers"])
app.include_router(ProducerController.router, tags=["consumers"])
