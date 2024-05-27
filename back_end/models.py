from enum import Enum
from sqlalchemy import Integer, String, Column, ForeignKey, Enum as EnumSQL, DateTime, Boolean
from sqlalchemy.orm import relationship

from datetime import datetime, timedelta, timezone

# from .database import Base
from back_end.database import Base

class User(Base):
    __tablename__ = "user_"

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False, unique=True)
    email = Column(String)
    password = Column(String, nullable=False) # hashed
    # created_at = Column(DateTime, default=datetime.utcnow) # UTC+3
    # updated_at = Column(DateTime, default=datetime.utcnow) # UTC+3
    created_at = Column(DateTime, default=lambda: datetime.now(timezone(timedelta(hours=3)))) # UTC+3
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone(timedelta(hours=3)))) # UTC+3

    task = relationship("Task", back_populates="user")
 
class task_status(Enum):
    done = "Done"
    not_done = "Not Done"

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    status = Column(EnumSQL(task_status), nullable=False)
    # status = Column(String, nullable?=False)
    # status = Column(bool, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone(timedelta(hours=3)))) # UTC+3
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone(timedelta(hours=3)))) # UTC+3
    user = relationship("User", back_populates="task")