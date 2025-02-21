from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.task import UserResponse, UserCreate
from crud import create_user, get_users

router = APIRouter()

@router.get("/", response_model=list[UserResponse])
async def read_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)

@router.post("/", response_model=UserResponse)
async def add_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)
