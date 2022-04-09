from fastapi import APIRouter

# library own
from schemal.user import User, UserLogin

app_auth = APIRouter()  


@app_auth.post('/login')
def login( user : UserLogin ):
    return user.dict()