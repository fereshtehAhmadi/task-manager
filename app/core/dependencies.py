from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import SessionLocal
from core.security import verify_password, create_access_token
from app.crud import get_user_by_username
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def authenticate_user(username: str, password: str, db: Session):
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.password_hash):
        return None
    return user
