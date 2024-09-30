import datetime
from typing import Annotated
from sqlalchemy import BigInteger, text, Identity
from sqlalchemy.orm import Mapped, mapped_column
from app.database.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
meta = Base.metadata

class UsersORM(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    vk_id: Mapped[int] = mapped_column(BigInteger, Identity())
    fullname: Mapped[str]
    photo_attachment: Mapped[str]
    photo_url: Mapped[str]
    download_count: Mapped[int] = mapped_column(default=0)
    day_download_count: Mapped[int] = mapped_column(default=20)
    resolution: Mapped[str] =mapped_column(default="1080p")
    created_at: Mapped[created_at]


class all_video(Base):
    __tablename__ = "video"

    uploader: Mapped[str]
    title: Mapped[str]
    description: Mapped[str]
    fulltitle: Mapped[str]
    thumbnail: Mapped[str]
    resolution: Mapped[str]
    webpageurl: Mapped[str]
    upload_date: Mapped[str]
    extractor: Mapped[str]   
