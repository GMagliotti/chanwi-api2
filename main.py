from typing import Union

from fastapi import FastAPI
from controllers import ConsumerController

app = FastAPI()
app.include_router(ConsumerController.router, tags=["consumers"])
