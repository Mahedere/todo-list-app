from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_task(db, skip=skip, limit=limit)
    return tasks

@app.post("/new_user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/user/{user_id}/new_task/", response_class=schemas.Task)
def create_task(user_id: int, task: schemas.Taskcreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task, user_id=user_id)