# main.py

from fastapi import FastAPI
from app.api import auth, s3
from app.models import user, s3_credentials  # Correct import order
from app.core.database import engine, get_db  # Import get_db for database access
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create tables
user.Base.metadata.create_all(bind=engine)
s3_credentials.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(s3.router, prefix="/s3")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI AWS S3 service"}
