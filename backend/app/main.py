#Import FastAPI
from fastapi import FastAPI

#Create a FastAPI instance. It will be the main point of interaction to create all the API
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}