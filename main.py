from typing import Union

from fastapi import FastAPI
from controllers import producerController,postController,receiverController, driveController, consumer_controller #, orderController

app = FastAPI()

app.include_router(producerController.router)
app.include_router(driveController.router)
app.include_router(receiverController.router)
app.include_router(consumer_controller.router)
app.include_router(postController.router)
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}