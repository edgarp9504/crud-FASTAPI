from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://nfonshujxdnibn:c7c0ec87f365e2a9c1ca2cedaa8853c4474917ab715f516f7b5e3beeb76375cd@ec2-34-192-210-139.compute-1.amazonaws.com/de19fghpjjde6i"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
