from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.task import TaskResponse, TaskCreate
from crud import get_tasks, create_task

router = APIRouter()

@router.get("/", response_model=list[TaskResponse])
async def read_tasks(db: AsyncSession = Depends(get_db)):
    return await get_tasks(db)

@router.post("/", response_model=TaskResponse)
async def add_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await create_task(db, task)
