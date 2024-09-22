import asyncio
from app.vk.main.handlers import download_labeler
from vkbottle import Bot 
from config import api, state_dispenser, labeler



labeler.load(download_labeler)

bot = Bot(
    api=api,
    labeler=labeler,
    state_dispenser=state_dispenser,
)

bot.run_forever()
