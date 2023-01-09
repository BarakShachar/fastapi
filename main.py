from fastapi import FastAPI, status, Form
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

load_dotenv()
cred_dict = {
    "type": os.getenv("type"),
    "project_id": os.getenv("project_id"),
    "private_key_id": os.getenv("private_key_id"),
    "private_key": os.getenv("private_key"),
    "client_email": os.getenv("client_email"),
    "client_id": os.getenv("client_id"),
    "auth_uri": os.getenv("auth_uri"),
    "token_uri": os.getenv("token_uri"),
    "auth_provider_x509_cert_url": os.getenv("auth_provider_x509_cert_url"),
    "client_x509_cert_url": os.getenv("client_x509_cert_url")
}

cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred)
db = firestore.client()
app = FastAPI()


@app.post("/signup/", status_code=status.HTTP_201_CREATED)
async def create_user(mail: str = Form(), isAdmin: str = Form(), name: str = Form()):
    doc_ref = db.collection("users").document(mail)
    doc_ref.set({
        "isAdmin": isAdmin,
        "name": name,
        "adminMail": None
    })
    return {"message": "user created successfully"}
