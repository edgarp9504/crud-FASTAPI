from datetime import datetime, timedelta
from fastapi import HTTPException
from jose import  jwt, JWTError

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

def expirate_jwt(days : int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date


def create_token(user : dict):
    return jwt.encode({**user, 'exp': expirate_jwt(2)}, SECRET_KEY, algorithm= ALGORITHM)

def verify_jwt(token = str):
    try:
        to_decode = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    
    except JWTError:
        raise HTTPException(status_code= 404, detail= 'token caucado')
    
    return to_decode 