# Running the server: uvicorn main:app --reload

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("authkey.json") 
firebase_admin.initialize_app(cred)
db = firestore.client()


#create a new document in firestore
def create_document(collection: str, document_data: dict):
    try:
        doc_ref = db.collection(collection).document()
        doc_ref.set(document_data)
        print('Document created with ID:', doc_ref.id)
    except Exception as e:
        print('An error occurred:', e)

    # #usage example
    # create_document('characters', {'name': 'John Doe', 'occupation': 'artist'})

def read_all_characters():
    try:
        docs = db.collection('characters').stream()
        list_of_characters = [] 
        for doc in docs:
            list_of_characters.append(doc.to_dict())
        return list_of_characters
    except Exception as e:
        print('An error occurred:', e)

def delete_character(id: str):
    try:
        db.collection('characters').document(id).delete()
        print('Document with ID:', id, 'deleted')
    except Exception as e:
        print('An error occurred, could not delete the character:', e)