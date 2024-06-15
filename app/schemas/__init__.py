from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    
class UserLogin(BaseModel):
    username: str
    password: str
    
class S3CredentialsCreate(BaseModel):
    access_key_id: str
    secret_access_key: str
    
class S3Item(BaseModel):
    item_name: str
    item_content: str