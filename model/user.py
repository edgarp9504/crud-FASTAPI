from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database.config import Base



class User(Base):
    __tablename__ =  "user"
    
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, unique = True ,index = True)
    email = Column(String, index = True)
    phone = Column(Integer, index = True)
    password = Column(String, index = True)