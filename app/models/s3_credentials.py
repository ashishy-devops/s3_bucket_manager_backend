from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from app.models.user import User

Base = declarative_base()

class S3Credentials(Base):
    __tablename__ = "s3_credentials"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id))
    access_key_id = Column(String)
    secret_access_key = Column(String)

