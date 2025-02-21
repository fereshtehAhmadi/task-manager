from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

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
