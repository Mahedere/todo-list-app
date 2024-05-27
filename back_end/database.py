from sqlalchemy import create_engine, schema, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

import os

load_dotenv()

# local database
# db_host = os.getenv("DB_HOST")
# db_name = os.getenv("DB_NAME")
# db_port = os.getenv("DB_PORT")
# db_user = os.getenv("DB_USER")
# db_password = os.getenv("DB_PASSWORD")

# render database
db_host = os.getenv("DB_HOST_re")
db_name = os.getenv("DB_NAME_re")
db_port = os.getenv("DB_PORT_re")
db_user = os.getenv("DB_USER_re")
db_password = os.getenv("DB_PASSWORD_re")



SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# metadata = MetaData(schema='new_schema')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()