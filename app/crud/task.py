from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.task import Task
from app.schemas.task import TaskCreate

async def create_task(db: AsyncSession, task: TaskCreate):
    new_task = Task(
        title=task.title,
        description=task.description,
        done=task.done,
        creator_id=task.creator_id,
        assignee_id=task.assignee_id
    )
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

async def get_tasks(db: AsyncSession):
    result = await db.execute(select(Task))
    return result.scalars().all()
