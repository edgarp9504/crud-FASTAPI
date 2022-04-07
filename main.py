from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_api():
    return 'Hola mundo'

@app.get('/api')
def get_api_hola():
    return 'Hola mundo FastAPI'