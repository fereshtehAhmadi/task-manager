from sqlalchemy import Column, DateTime, Boolean, func, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr
from database import Base


class BaseModel(Base):
    __abstract__ = True

    is_active = Column(Boolean, default=True)
    creation_datetime = Column(DateTime, default=func.now())
    update_datetime = Column(DateTime, default=func.now(), onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

class User(BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_tasks = relationship("Task", back_populates="creator", foreign_keys="[Task.creator_id]")
    assigned_tasks = relationship("Task", back_populates="assignee", foreign_keys="[Task.assignee_id]")

class Task(BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    done = Column(Boolean, default=False)
    creator_id = Column(Integer, ForeignKey("user.id"))
    assignee_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    creator = relationship("User", back_populates="created_tasks", foreign_keys=[creator_id])
    assignee = relationship("User", back_populates="assigned_tasks", foreign_keys=[assignee_id])
