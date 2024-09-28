from typing import Annotated
from sqlalchemy import String
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
)

session = async_sessionmaker(engine)

str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
	type_annotation_map={
		str_256: String(256)
	}
