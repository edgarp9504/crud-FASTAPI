from fastapi import HTTPException
from sqlalchemy.orm import Session

# own library
from middleware.jwtsecurity import create_token
import model.user as Model
import schemal.user as Schemal
from middleware.password import hashed_password, verify_password


def login(db : Session,email : str , password : str):
    
    if get_user_by_email( email = email, db= db) is None:
        raise HTTPException(status_code= 404, detail= 'email no existe')
        
    user = db.query(Model.User).filter(Model.User.email == email).first()
    
    if verify_password(password, user.password) is False:
        raise HTTPException(status_code= 404, detail= 'password es incorrecto')    
    
    jwt = create_token({'username': user.username, 'email' : user.email} )
    
    to_encode = user.__dict__
    
    del to_encode['_sa_instance_state']
    
    print(to_encode.update({'token' : jwt}))
    
    return to_encode


def get_user_by_email(  email : str, db = Session):   
    return db.query(Model.User).filter(Model.User.email == email).first()



def create_user(user : Schemal.UserRegister , db = Session):
    
    try:
        
        if get_user_by_email( email=user.email, db= db):
            raise HTTPException(status_code= 404, detail= 'email already register')
        
        db_user = Model.User( email = user.email, username = user.username, phone = user.phone, password =hashed_password(user.password) )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

    except:
        raise HTTPException(status_code= 404, detail= 'Erro al registrar usuario')

    return 'Usuario registrado con exito'

def get_users( db : Session,  skip: int = 0, limit: int = 100):
    query = db.query(Model.User.id, Model.User.username, Model.User.email, Model.User.phone)
    return query.offset(skip).limit(limit).all()