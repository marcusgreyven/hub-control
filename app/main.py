from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.services.system_info import get_system_info

app = FastAPI()

@app.get("/api/system")
def system_info():
    return get_system_info()

app.mount("/", StaticFiles(directory = "static", html = True), name = "static")