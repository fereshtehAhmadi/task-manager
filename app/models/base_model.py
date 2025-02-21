from sqlalchemy import Column, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declared_attr
from app.database import Base


class BaseModel(Base):
    __abstract__ = True

    is_active = Column(Boolean, default=True)
    creation_datetime = Column(DateTime, default=func.now())
    update_datetime = Column(DateTime, default=func.now(), onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
