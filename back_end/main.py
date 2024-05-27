from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
# from fastapi.middleware.cors import CORSMiddleware
import logging
# import uvicorn
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from back_end import crud, models, schemas
from back_end.database import SessionLocal, engine
from back_end.models import task_status

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def main_():
    """
    test endpoint
    """
    return "To do list app API"

# this should be only for admin 
# @app.get("/all_tasks/", response_model=list[schemas.Task])
# def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     tasks = crud.get_task(db, skip=skip, limit=limit)
#     return tasks

# commented this out because currently not using any of this endpoints
# @app.post("/new_user/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     """
#     """
#     db_user = crud.get_user_by_email(db, user_name=user.user_name)
#     if db_user:
#         raise HTTPException(status_code=400, detail="user name already registered")
#     return crud.create_user(db=db, user=user)

# @app.post("/user/{user_id}/new_task/", response_model=schemas.Task)
# def create_task(user_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
#     """
#     - This is to create new task for user of user_id
#     - user_id has tobe loggedin inorder to create task for user_id
#     """
#     return crud.create_task(db=db, user_id=user_id, task=task)

# @app.get("/tasks/", response_model=list[schemas.Task])
# def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     tasks = crud.get_tasks(db, skip=skip, limit=limit)
#     return tasks

@app.post("/task/", response_model=schemas.Task)
def create_task_default(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """ Creates new task with id 1 which i am considering as default user
    task: task that is going to be created with schema type of TaskCreate
    db: database session
    Return: the created task
    """
    task.user_id = 1
    print("[INFO] task type", type(task))
    return crud.create_task(db=db, task=task)

@app.get("/tasks/", response_model=list[schemas.Task])
def read_task(db: Session = Depends(get_db)):
    """Reads tasks list with id 1 which i am considering as default user
    db: database session
    Return: lists of tasks with id of 1
    """
    user_id = 1
    return crud.my_tasks(db, user_id = user_id)

# logging.basicConfig(level=logging.DEBUG)
