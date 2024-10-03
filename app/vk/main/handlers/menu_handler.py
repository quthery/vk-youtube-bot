from vkbottle.bot import BotLabeler, Message
from vkbottle import template_gen, TemplateElement, Keyboard, OpenLink, KeyboardButtonColor
from app.database import repo
from app.vk.keyboard.keyboard import start_keyboard
from config import settings

menu_labeler = BotLabeler()



@menu_labeler.private_message(text="Профиль 🪪")
async def profile(message: Message):
    user = await repo.get_user(int(message.from_id))
    user_vk = await settings.user_api.users.get(user_ids=[message.from_id], 
        fields=["photo_max", "photo_id"])
    keyboard = Keyboard().add(OpenLink(link=f"https://vk.com/fetchtube", label="👤Страница"))
    if user != None:
        msg = f"{user.fullname}\n\n"
        msg += f"Доступно скачиваний {user.download_count}\n"
        msg += f"Видео скачано {user.day_download_count}\n"
        msg += f"Зарегисрирован {user.created_at}\n"
        await message.answer(msg, keyboard=start_keyboard)
    else:
        
        await repo.add_user( 
            id=message.from_id,
            full_name=user_vk[0].first_name + " "+ user_vk[0].last_name,
            photo_attachment=user_vk[0].photo_max,
            photo_url=user_vk[0].photo_id
        )
        user = await repo.get_user(int(message.from_id))
        msg = f"Имя {user.fullname}\n\n"
        msg += f"Доступно скачиваний {user.download_count}\n"
        msg += f"Видео скачано {user.day_download_count}\n"
        msg += f"Зарегисрирован {user.created_at}\n"
        
        await message.answer(msg, keyboard=start_keyboard)


@menu_labeler.private_message(text="Скачать видео")
async def remove_count(message: Message):
    await repo.remove_user_count(int(message.from_id))
    await message.answer("Скачать видео успешно")