from sqlalchemy import  Column,Integer, String, Enum, Boolean

from database.config import Base, SessionLocal, engine
from schemal.roles import UserRoles

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

class User(Base):
    __tablename__ =  "user"
    
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, unique = True ,index = True)
    email = Column(String, index = True)
    phone = Column(Integer, index = True)
    password = Column(String, index = True)
    user_role = Column(Enum(UserRoles),server_default = UserRoles.user.name, index = True)
    activate_user = Column(Boolean, index = True)
    

