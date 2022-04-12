from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email : EmailStr
    
class UserLogin(User):
    password : str   
    
class UserBase(User):
    id : int | None
    username : str | None
    phone : int | None
    
    class Config:
        orm_mode = True

class UserToken(UserBase):
    token : str

class UserRegister(UserBase):
    password : str 