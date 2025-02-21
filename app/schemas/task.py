from pydantic import BaseModel
from typing import Optional
from .user import UserResponse

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False

class TaskCreate(TaskBase):
    creator_id: int
    assignee_id: int

class TaskResponse(TaskBase):
    id: int
    creator: UserResponse
    assignee: Optional[UserResponse] = None

    class Config:
        from_attributes = True
