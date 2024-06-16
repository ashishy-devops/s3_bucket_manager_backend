import boto3
from sqlalchemy.orm import Session
from app.models.s3_credentials import S3Credentials
from app.schemas import S3CredentialsCreate
from fastapi import UploadFile, HTTPException

def store_s3_credentials(db: Session, user, credentials: S3CredentialsCreate):
    db_credentials = S3Credentials(
        user_id=user.id,
        access_key_id=credentials.access_key_id,
        secret_access_key=credentials.secret_access_key
    )
    db.add(db_credentials)
    db.commit()
    db.refresh(db_credentials)
    return db_credentials

def update_s3_credentials(credentials: S3CredentialsCreate, db: Session, user):
    db_credentials = db.query(S3Credentials).filter(S3Credentials.user_id == user.id).first()
    if db_credentials:
        db_credentials.access_key_id = credentials.access_key_id
        db_credentials.secret_access_key = credentials.secret_access_key
        db.commit()
        db.refresh(db_credentials)
        return db_credentials
    else:
        return None
    
def delete_s3_credentials(db: Session, user):
    db_credentials = db.query(S3Credentials).filter(S3Credentials.user_id == user.id).first()
    if db_credentials:
        db.delete(db_credentials)
        db.commit()
        return True
    else:
        return False
    
def get_s3_client(db: Session, user):
    db_credentials = db.query(S3Credentials).filter(S3Credentials.user_id == user.id).first()
    if db_credentials:
        return boto3.client(
            's3',
            aws_access_key_id=db_credentials.access_key_id,
            aws_secret_access_key=db_credentials.secret_access_key
        )
    else:
        return None
    
def list_buckets(db: Session, user):
    client = get_s3_client(db, user)
    if client:
        response = client.list_buckets()
        return response.get('Buckets', [])
    else:
        return []

def list_items(bucket_name: str, db: Session, user):
    client = get_s3_client(db, user)
    if client:
        response = client.list_objects_v2(Bucket=bucket_name)
        return response.get('Contents', [])
    else:
        return []
    
def add_item(bucket_name: str, item_name: str, db: Session, user, file: UploadFile):
    client = get_s3_client(db, user)
    if client:
        file_obj = file.file
        client.put_object(Bucket=bucket_name, Key=item_name, Body=file_obj)
        return {"message": "File uploaded successfully"}
    else:
        return {"error": "Failed to upload file"}
    

def delete_item(bucket_name: str, item_name: str, db: Session, user):
    client = get_s3_client(db, user)
    if client:
        client.delete_object(bucket_name=bucket_name, Key=item_name)
        return {"message": "Item deleted Successfully"}
    else:
        return {"error": "Failed to delete item"}
    
def add_bucket(bucket_name: str, db: Session, user):
    client = get_s3_client(db, user)
    if client:
        try:
            client.create_bucket(Bucket=bucket_name)
            return {"message": "Bucket Created successfully"}
        except client.exceptions.BucketAlreadyExists:
            raise HTTPException(status_code=400, detail="Bucket already exists")
        except client.exceptions.BucketAlreadyOwnedByYou:
            raise HTTPException(status_code=400, detail="Bucket already owned by you")
    else:
        raise HTTPException(status_code=400, detail="Failed to create bucket")
    
def remove_bucket(bucket_name: str, db: Session, user):
    client = get_s3_client(db, user)
    if client:
        try:
            client.delete_bucket(Bucket=bucket_name)
            return {"message": "Bucket deleted successfully"}
        except client.exceptions.NoSuchBucket:
            raise HTTPException(status_code=400, detail="Bucket not found")
    else:
        raise HTTPException(status_code=400, detail="Failed to delete bucket")
        