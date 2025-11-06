from fastapi import FastAPI, HTTPException


app = FastAPI()

@app.get(path="/")
def home():
    return "Hello, Darling"