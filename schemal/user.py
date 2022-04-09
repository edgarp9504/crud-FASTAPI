from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email : EmailStr
    
class UserLogin(User):
    password : str   
    
class UserBase(User):
    username : str | None
    phone : int | None
    
class UserRegister(UserBase):
    password : str 