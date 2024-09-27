from app.vk.main import download_labeler, start_labeler, menu_labeler 
from vkbottle import Bot 
from app.database.create_tables import create_tables
from config import settings, labeler, state_dispenser
import asyncio

async def main():
    labeler.load(menu_labeler)
    labeler.load(start_labeler)
    labeler.load(download_labeler)

    bot = Bot(
        api=settings.main_bot,
        labeler=labeler,
        state_dispenser=state_dispenser,
    )
    await create_tables()
    await bot.run_polling()

asyncio.run(main())
