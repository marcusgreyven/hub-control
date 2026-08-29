from fastapi import FastAPI

app = FastAPI()
@app.get("/")

def root():
    return {
  "hostname": "hub",
  "temperature": 41.8,
  "cpu_percent": 12.4,
  "memory_available_mb": 704,
  "disk_free_gb": 22.8,
  "uptime_seconds": 18432
}