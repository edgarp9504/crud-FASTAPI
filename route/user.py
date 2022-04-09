from statistics import mode
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# own library
import model.user as Models
import schemal.user as Schemal
from database.config import SessionLocal, engine
import crud.user as Crud

Models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()
        


app_user = APIRouter()

@app_user.get('/user')
def get_user(db : Session = Depends(get_db)):
    return Crud.get_users(db)

@app_user.post('/user')
def create_user( model : Schemal.UserRegister, db : Session = Depends(get_db)):
    return Crud.create_user(db=db, user=model)

@app_user.delete('/user')
def delete_user():
    return 'DELETE-USER | FASTAPI '

@app_user.put('/user')
def update_user():
    return 'PUT-USER | FASTAPI '