from typing import Union
from fastapi import FastAPI, Request
from firebase import create_document, read_all_characters, delete_character_firebase

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
    create_document("npc", data)
    return {"status": "success"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# In order to code to work, do not give same function name as in the firebase.py file. 
# Ex: below function called delete_character_endpoint and in firebase.py -> delete_character_firebase
@app.delete("/delete_character") 
async def delete_character_endpoint(request: Request): 
    try:
        data = await request.json()
        character_id = data.get('id')
        await delete_character_firebase(character_id)
        return {"status": "success", "message": f"Character with ID {character_id} deleted successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}