from statistics import mode
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# own library
import model.user as Models
import schemal.user as Schemal
import crud.user as Crud
from route.auth import oauth2_scheme


app_user = APIRouter()

@app_user.get('/user')
def get_user(db : Session = Depends(Models.get_db), token = Depends(oauth2_scheme)):
    return Crud.get_users(db)

@app_user.post('/user')
def create_user( model : Schemal.UserRegister, db : Session = Depends(Models.get_db), token = Depends(oauth2_scheme)):
    return Crud.create_user(db=db, user=model)

@app_user.delete('/user')
def delete_user(token = Depends(oauth2_scheme)):
    return 'DELETE-USER | FASTAPI '

@app_user.put('/user')
def update_user(token = Depends(oauth2_scheme)):
    return 'PUT-USER | FASTAPI '