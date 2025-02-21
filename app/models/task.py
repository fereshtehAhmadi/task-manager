from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .base_model import BaseModel


class Task(BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    done = Column(Boolean, default=False)
    creator_id = Column(Integer, ForeignKey("user.id"))
    assignee_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    creator = relationship("User", back_populates="created_tasks", foreign_keys=[creator_id])
    assignee = relationship("User", back_populates="assigned_tasks", foreign_keys=[assignee_id])
