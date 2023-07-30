from fastapi import FastAPI

app = FastAPI()

@app.get('/helloworld')
def get_hello_message():
    return {"message": "Hello World!!"}