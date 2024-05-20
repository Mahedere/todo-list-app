# here the pydantic models
import datetime
from pydantic import BaseModel

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

# Task
class TaskBase(BaseModel):
    book_id: int
    name: str
    description: str
    status: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True