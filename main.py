from typing import Union

from fastapi import FastAPI
from controllers import producerController,postController,orderController,receiverController

app = FastAPI()

app.include_router(producerController.router, prefix="/producer", tags=["producer"])
app.include_router(postController.router, prefix="/post", tags=["post"])
app.include_router(orderController.router, prefix="/order", tags=["order"])
app.include_router(receiverController.router, prefix="/receivers", tags=["receiver"])
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}