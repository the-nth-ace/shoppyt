import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

DATABASE_URL = os.environ["DATABSE_URL"]
engine = create_async_engine(DATABASE_URL)

async_session = sessionmaker(autocommit=False, expire_on_commit=False, class_=AsyncSession, autoflush=False, bind=engine)


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        async with session.begin():
            try:
                yield session
            finally:
                await session.close()


Base = declarative_base()
