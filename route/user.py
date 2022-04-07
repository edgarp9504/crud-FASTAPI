from fastapi import APIRouter

app_user = APIRouter()

@app_user.get('/user')
def get_user():
    return 'GET-USER | FASTAPI '

@app_user.post('/user')
def create_user():
    return 'POST-USER | FASTAPI '

@app_user.delete('/user')
def delete_user():
    return 'DELETE-USER | FASTAPI '

@app_user.put('/user')
def update_user():
    return 'PUT-USER | FASTAPI '