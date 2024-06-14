from fastapi import APIRouter, Depends
from schemas import UserLogin
from app.services.auth_service import login_user, logout_user

router = APIRouter()

@router.post("/login")
def login(user: UserLogin):
    return login_user(user)

@router.post("/logout")
def logout(token: str):
    return logout_user(token)