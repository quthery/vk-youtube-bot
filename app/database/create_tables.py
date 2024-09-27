from app.database import meta
from app.database import engine

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(meta.create_all)
