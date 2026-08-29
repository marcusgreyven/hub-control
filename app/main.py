from fastapi import FastAPI
from app.services.system_info import get_system_info

app = FastAPI()

@app.get("/")
def root():
    return get_system_info()