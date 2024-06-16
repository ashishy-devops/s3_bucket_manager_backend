from fastapi import FastAPI
from app.api import auth, s3
from app.models import user
from app.core.database import engine
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


user.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(s3.router, prefix="/s3")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI AWS S3 service"}