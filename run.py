from app.vk.main import download_labeler, start_labeler, menu_labeler 
from vkbottle import Bot 
from config import state_dispenser, labeler, main_group_api


labeler.load(menu_labeler)
labeler.load(start_labeler)
labeler.load(download_labeler)

bot = Bot(
    api=main_group_api,
    labeler=labeler,
    state_dispenser=state_dispenser,
)

bot.run_forever()
