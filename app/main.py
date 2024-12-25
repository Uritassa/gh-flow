import uvicorn
from fastapi import FastAPI, Body, Response, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to gh-flow demo"}

@app.get("/healthz")
def healthz():
    return {"status": "ok", "database": "connected"}

@app.get("/ready")
def healthz():
    return {"status": "ok", "app": "ready"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True) 

