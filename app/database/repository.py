from app.database import new_session
from app.database import UsersORM
from sqlalchemy import select, update


class Repository:
    @classmethod
    async def add_user(cls, id: int, full_name: str, photo_attachment: str,
     photo_url: str):
        async with new_session() as session:
            user = UsersORM(vk_id=id , 
            fullname=full_name, 
            photo_attachment=photo_attachment, 
            photo_url=photo_url
            )
            session.add(user)
            await session.commit()

    @classmethod
    async def get_user(cls, vk_id: int):
        async with new_session() as session:
          query = select(UsersORM).filter_by(vk_id=vk_id)

          result = await session.execute(query)
          return result.scalar()

    @classmethod
    async def get_users(cls):
        async with new_session() as session:
            query = select(UsersORM)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def remove_user_count(cls, vk_id: int):
        async with new_session() as session:
            query = update(UsersORM).where(UsersORM.vk_id == vk_id).values(download_count=UsersORM.download_count+1, day_download_count=UsersORM.day_download_count-1)
            await session.execute(query)
            await session.commit()

            
