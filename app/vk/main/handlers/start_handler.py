from vkbottle.bot import BotLabeler, Message
from app.vk.keyboard.keyboard import start_keyboard

start_labeler = BotLabeler()


@start_labeler.private_message(text="Начать")
async def start_message(message: Message):
    await message.answer("Привет ты попал в бота FetchTube\nПросто отправь мне ссылку на видео\nИли используй для навигации кнопки ниже", keyboard=start_keyboard)
   

@start_labeler.private_message(command="start")
async def start_command(message: Message):
    await message.answer("Привет ты попал в бота FetchTube\nПросто отправь мне ссылку на видео\nИли используй для навигации кнопки ниже", keyboard=start_keyboard)
