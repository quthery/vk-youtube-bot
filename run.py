from app.vk.main import download_labeler, start_labeler, menu_labeler 
from vkbottle import Bot 
from config import settings, labeler, state_dispenser
from app.database import create_tables
# import asyncio
# async def main():
#     await create_tables()
#
# asyncio.run(main())
labeler.load(menu_labeler)
labeler.load(start_labeler)
labeler.load(download_labeler)

bot = Bot(
    api=settings.main_bot,
    labeler=labeler,
    state_dispenser=state_dispenser,
)


bot.run_forever()
