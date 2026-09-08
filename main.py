from fastapi import FastAPI

app = FastAPI(title="Ta'lim.Neon API")

@app.get("/")
def read_root():
    return {"status": "active", "platform": "Ta'lim.Neon API ishlamoqda"}
  
