from vkbottle.bot import BotLabeler, Message

menu_labeler = BotLabeler()



@menu_labeler.private_message(text="Профиль 🪪")
async def profile(message: Message):
    await message.answer("hello world")
