from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str
    
class S3Credentials(BaseModel):
    accessKeyId: str
    secretAccessKey: str
    
class S3Item(BaseModel):
    itemName: str
    itemContent: str