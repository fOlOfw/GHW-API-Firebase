from typing import Union
from fastapi import FastAPI, Request
from firebase import create_document, read_all_characters


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/characters")
async def read_characters():
    return {"characters": read_all_characters()}

@app.post("/add_character")
async def add_character(request: Request): 
    data = await request.json()
    print("character added: ", data)
    create_document("people", data)
    return {"status": "success"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.delete("/delete_character")
async def delete_character(request: Request):
    data = await request.json()
    print("character deleted: ", data)
    delete_character(data['id'])
    return {"status": "success"}