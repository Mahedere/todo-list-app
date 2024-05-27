# here the pydantic models
import datetime
from pydantic import BaseModel
from back_end.models import task_status
from typing import List

# User
class UserBase(BaseModel):
    user_name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

# Task
class TaskBase(BaseModel):
    user_id: int
    name: str
    description: str
    status: task_status

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True