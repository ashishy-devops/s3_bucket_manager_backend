from fastapi import FastAPI
from app.api import auth, s3

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(s3.router, prefix="/s3")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI AWS S3 service"}