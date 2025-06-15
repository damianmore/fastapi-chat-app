from fastapi import FastAPI

app = FastAPI(title='fast api',description = 'this is my fast api')

@app.get('/hello')
def hello():
    return {'msg':'hello'}