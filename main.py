from fastapi import FastAPI, status
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(".env")
firebase_admin.initialize_app(cred)
db = firestore.client()
app = FastAPI()


class User(BaseModel):
    mail: str
    name: str
    isAdmin: bool


@app.post("/signup/", status_code=status.HTTP_201_CREATED)
async def demo_post(user: User):
    doc_ref = db.ollection("users").document(user.mail)
    doc_ref.set({
        "isAdmin": user.isAdmin,
        "name": user.name,
        "adminMail": None
    })
    return {"message": "user created successfully"}
