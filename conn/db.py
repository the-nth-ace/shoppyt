import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

DATABASE_URL = os.environ["DATABSE_URL"]
engine = create_engine(DATABASE_URL)

db_sesssion = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


Base = declarative_base()
