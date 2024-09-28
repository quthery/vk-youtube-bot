from app.database import new_session
from app.database import UsersORM
from sqlalchemy import select




class Repository:
    @classmethod
    async def add_user(cls, id: int, full_name: str, photo_attachment: str, photo_url: str):
        async with new_session() as session:
            user = UsersORM(vk_id=id , full_name=full_name, photo_attachment=photo_attachment, photo_url=photo_url)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def get_user(cls, vk_id: int):
        async with new_session() as session:
          query = select(UsersORM).filter_by(vk_id=vk_id)

          result = await session.execute(query)
          return result.scalars().first()

    @classmethod
    async def get_users(cls):
        async with new_session() as session:
            query = select(UsersORM)
            result = await session.execute(query)
            return result.scalar_or_none()
