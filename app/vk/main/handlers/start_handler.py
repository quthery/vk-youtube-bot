from vkbottle.bot import BotLabeler, Message
from app.vk.keyboard.keyboard import start_keyboard
from app.database import repo
from config import settings

start_labeler = BotLabeler()


@start_labeler.private_message(text="Начать")
async def start_message(message: Message):
		user = await settings.user_api.users.get(user_ids=[message.from_id], fields=["photo_max", "photo_id"])
		await repo.add_user(id=message.from_id, full_name=user.first_name++user.last_name, photo_attachment=user.photo_max, photo_url=user.photo_id)
    await message.answer("Привет ты попал в бота FetchTube\nПросто отправь мне ссылку на видео\nИли используй для навигации кнопки ниже", keyboard=start_keyboard)


@start_labeler.private_message(command="start")
async def start_command(message: Message):
    await message.answer("Привет ты попал в бота FetchTube\nПросто отправь мне ссылку на видео\nИли используй для навигации кнопки ниже", keyboard=start_keyboard)
