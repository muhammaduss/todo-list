import os
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

engine = create_async_engine(
    url=f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
    + f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}"
    + f"/{os.getenv('DB_NAME')}",
    echo=True,
)

session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
