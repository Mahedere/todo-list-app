from sqlalchemy.orm import Session
import bcrypt

from back_end import models, schemas

# hash
def hash_password(password):
    password_bytes = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_password.decode("utf-8")

# get user by id
def get_user(db: Session, user_id: int):
    """
    db:  database session
    user_id -- the user id
    Return: single user data
    """
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, user_name: str):
    """ get the first user with user_name of given user_name
    - used later to avoid user duplication
    """
    return db.query(models.User).filter(models.User.user_name == user_name).first()

# get all users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    db:  database session
    skip: the lower limit
    limit: the upper limit
    user_id -- the user id
    Return: single user data
    """
    return db.query(models.User).offset(skip).limit(limit).all()

# create user
def create_user(db: Session, user: schemas.UserCreate):
    """
    db: database session
    user: user data
    Return: returns created user data
    """
    hashed_password = hash_password(user.password)
    db_user = models.User(user_name=user.user_name, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print("[INFO] db_user", db_user)
    return db_user

# get all tasks
def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    """
    db:  database session
    skip: the lower limit
    limit: the upper limit
    Return: all tasks
    """
    return db.query(models.Task).offset(skip).limit(limit).all()

def my_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    """
    db:  database session
    user_id -- the user id
    Return: all tasks with Task.user_id == user_id
    """
    tasks = db.query(models.Task).filter(models.Task.user_id == user_id).offset(skip).limit(limit).all()

    return tasks

# create task
def create_task(db: Session, task: schemas.TaskCreate):
    """
    db: database session
    task: task data
    user_id: user id where the task is going to be crated for
    Return: returns created task data
    """
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task