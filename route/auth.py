from typing import Optional
from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import  jwt, JWTError

# library own
from schemal.user import  UserToken
import crud.user  as Crud
import model.user as Models

app_auth = APIRouter()  

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login") 


@app_auth.post('/login', response_model= UserToken)
def login( form_data: OAuth2PasswordRequestForm = Depends(), db : Session() = Depends(Models.get_db) ):
    return Crud.login(email=form_data.username, password= form_data.password , db=db)