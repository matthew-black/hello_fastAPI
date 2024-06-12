# https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI
# Note: FastAPI is a class that inherits directly from Starlette:
  # https://www.starlette.io

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}
