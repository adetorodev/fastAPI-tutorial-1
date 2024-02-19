from fastapi import FastAPI, HTTPException
from pathlib import Path
from pydantic import BaseModel, PositiveInt
from datetime import datetime
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get('/')
async def root():
    return {"message": "Welcome to FastAPI"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/docs/{file_path:path}")
async def read_file(file_path: str):
    file_location = Path('docs') / file_path
    if not file_location.exist() or not file_location.is_file():
        raise HTTPException(status_code=404, detail= "file not found" )
    
    with open(file_location, 'r') as file:
        content = file.read()
    
    return {'content': content}

# @app.get("/docs/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}
