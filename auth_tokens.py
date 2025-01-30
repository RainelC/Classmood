from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from dotenv import load_dotenv
from db import *
import os 
from serialize import serialize_doc


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
load_dotenv()
key_secret = os.getenv("key_jwt")

def enconde_token(payload: dict) -> str:
    token = jwt.encode(payload, key_secret, algorithm='HS256')
    return token

def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    data = jwt.decode(token, key_secret, algorithms=['HS256'])
    user = db.teachers.find_one({"email": data["email"]})
    return serialize_doc(user)

db, fs, collection = conexion_db()

