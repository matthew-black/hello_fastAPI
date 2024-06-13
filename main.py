# https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI
# Note: FastAPI is a class that inherits directly from Starlette:
    # https://www.starlette.io

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # If the item_id param can't be parsed as an int, this route
    # will respond with 422 and { detail: [ {errorObject} ] }
    return {"item_id": item_id}

