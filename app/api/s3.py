from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from app.schemas import S3CredentialsCreate, S3BucketCreate
from app.services.s3_service import (
    list_buckets, list_items, add_item, delete_item,
    store_s3_credentials, update_s3_credentials, delete_s3_credentials,
    add_bucket, remove_bucket, download_item
)
from app.services.auth_service import get_current_user
from app.core.database import get_db
import mimetypes

router = APIRouter()

@router.post("/credentials")
def add_s3_credentials(credentials: S3CredentialsCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return store_s3_credentials(db, current_user, credentials)

@router.put("/credentials")
def put_s3_credentials(credentials: S3CredentialsCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return update_s3_credentials(credentials, db, current_user)

@router.delete("/credentials")
def remove_s3_credentials(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return delete_s3_credentials(db, current_user)

@router.get("/buckets")
def get_buckets(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return list_buckets(db, current_user)

@router.get("/buckets/{bucket_name}")
def get_items(bucket_name: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return list_items(bucket_name, db, current_user)

@router.post("/buckets/{bucket_name}/items")
def upload_item(bucket_name: str, db: Session = Depends(get_db), current_user = Depends(get_current_user), file: UploadFile = File(...)):
    return add_item(bucket_name, db, current_user, file)

@router.get("/buckets/{bucket_name}/items/{item_name}")
def download_item_route(bucket_name: str, item_name: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    file_stream = download_item(bucket_name, item_name, db, current_user)
    if not file_stream:
        raise HTTPException(status_code=404, detail="Item not found")
    
    mime_type, _ = mimetypes.guess_type(item_name)
    if mime_type is None:
        mime_type = "application/octet-stream"
    
    return StreamingResponse(file_stream, media_type=mime_type, headers={"Content-Disposition": f"attachment; filename={item_name}"})

@router.delete("/buckets/{bucket_name}/items/{item_name}")
def remove_item(bucket_name: str, item_name: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return delete_item(bucket_name, item_name, db, current_user)

@router.post("/buckets")
def create_bucket(bucket: S3BucketCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return add_bucket(bucket.bucket_name, db, current_user)

@router.delete("/buckets/{bucket_name}")
def delete_bucket(bucket_name: str, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return remove_bucket(bucket_name, db, current_user)