from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_api():
    return 'Hola mundo'