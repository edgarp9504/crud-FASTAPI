
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email : EmailStr

class UserBase(User):
    id : int | None
    username : str | None
    phone : int | None
    perfil : str | None
    is_active : bool | None
    
    class Config:
        orm_mode = True

class UserToken(UserBase):
    token : str

class UserRegister(UserBase):
    password : str 