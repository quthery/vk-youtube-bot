from vkbottle.bot import BotLabeler, Message
from app.database import repo
menu_labeler = BotLabeler()



@menu_labeler.private_message(text="Профиль 🪪")
async def profile(message: Message):
    user = await repo.get_user(int(message.from_id))
    msg = f"Имя {user.fullname}\n\n"
    msg += f"Видео скачано {user.download_count}\n"
    msg += f"Зарегисрирован {user.created_at}\n"
    
    await message.answer(msg, attachment=f"photo{user.photo_url}")
