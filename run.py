import asyncio
from app.vk.main.handlers import download_labeler
from vkbottle import Bot 
from config import api, state_dispenser, labeler, main_group_api



labeler.load(download_labeler)

bot = Bot(
    api=main_group_api,
    labeler=labeler,
    state_dispenser=state_dispenser,
)

bot.run_forever()
