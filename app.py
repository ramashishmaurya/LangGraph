from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI()

@app.get("/")
def getdata():
    return{
        "datareturn" :"put data is comming okay"
    }


