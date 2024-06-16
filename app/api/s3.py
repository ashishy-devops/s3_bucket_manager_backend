from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.schemas import S3CredentialsCreate, S3BucketCreate
from app.services.s3_service import (
    list_buckets, list_items, add_item, delete_item,
    store_s3_credentials, update_s3_credentials, delete_s3_credentials,
    add_bucket, remove_bucket
)
from app.services.auth_service import get_current_user
from app.core.database import get_db

router = APIRouter()

@router.post("/credentials")
def add_s3_credentials(credentials: S3CredentialsCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return store_s3_credentials(db, current_user, credentials)

@router.put("/credentials")
def update_s3_credentials(credentials: S3CredentialsCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return update_s3_credentials(db, current_user, credentials)

@router.delete("/credentials")
def delete_s3_credentials(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return delete_s3_credentials(db, current_user)

@router.get("/buckets")
def get_buckets(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return list_buckets(db, current_user)

@router.get("/buckets/{bucket_name}")
def get_items(bucket_name: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return list_items(bucket_name, db, current_user)

@router.post("/bucekts/{bucekt_name}/items")
def upload_item(bucket_name: str, db: Session = Depends(get_db), current_user = Depends(get_current_user), item_name: str, file: UploadFile = File(...)):
    return add_item(bucket_name, db, current_user, item_name, file)

@router.delete("/bucket/{bucket_name}/items/{item_name}")
def delete_item(bucket_name: str, item_name: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return delete_item(bucket_name, item_name, db, current_user)

@router.post("/buckets")
def create_bucket(bucket: S3BucketCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return add_bucket(bucket.bucket_name, db, current_user)

@router.delete("/buckets/{bucket_name}")
def remove_bucket(bucket_name: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return remove_bucket(bucket_name, db, current_user)