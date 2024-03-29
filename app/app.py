from fastapi import FastAPI, Request, Response
from sqlalchemy import null

# own library
from route.auth import app_auth
from route.user import app_user
from database.config import SessionLocal

app = FastAPI()

# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#         print(request.state.db)
#     finally:
#         request.state.db.close()
#     return response


app.include_router(app_auth, tags=['login'])
app.include_router(app_user, tags=['Users'], prefix="/api")
