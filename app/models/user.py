from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base_model import BaseModel

class User(BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_tasks = relationship("Task", back_populates="creator", foreign_keys="[Task.creator_id]")
    assigned_tasks = relationship("Task", back_populates="assignee", foreign_keys="[Task.assignee_id]")

