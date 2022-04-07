from fastapi import APIRouter

app_auth = APIRouter()  


@app_auth.post('/login')
def login():
    return 'Login | FastAPI'