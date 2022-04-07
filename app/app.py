from fastapi import FastAPI

# own library
from route.auth import app_auth
from route.user import app_user

app = FastAPI()

app.include_router(app_auth, tags=['login'])
app.include_router(app_user, tags=['Users'], prefix="/api")
