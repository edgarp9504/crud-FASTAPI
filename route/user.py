from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from middleware.role import is_admin

# own library

import model.user as Models
from schemal.roles import UserRoles
import schemal.user as Schemal
import crud.user as Crud
from middleware.jwtsecurity import verify_jwt
from route.auth import oauth2_scheme


app_user = APIRouter()

 
    
    
@app_user.get('/user' )
def get_user(db : Session = Depends(Models.get_db), token = Depends(oauth2_scheme)):
    if is_admin(token, db) is False:
        raise HTTPException(status_code= 403, detail= 'Usuario sin permiso')
    return Crud.get_users(db)

  
@app_user.post('/user')
def create_user( model : Schemal.UserRegister, db : Session = Depends(Models.get_db), token = Depends(oauth2_scheme)):
    return Crud.create_user(db=db, user=model)


@app_user.delete('/user')
def delete_user(db : Session = Depends(Models.get_db), token = Depends(oauth2_scheme)):
    if is_admin(token, db) is False:
        raise HTTPException(status_code= 403, detail= 'Usuario sin permiso')
    return 'DELETE-USER | FASTAPI '

@app_user.put('/user')
def update_user(db : Session = Depends(Models.get_db), token = Depends(oauth2_scheme)):
    if is_admin(token, db) is False:
        raise HTTPException(status_code= 403, detail= 'Usuario sin permiso')
    return 'PUT-USER | FASTAPI '
