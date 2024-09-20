from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink, Location



async def keyboard(youtube_link: str):
    keyboard = Keyboard(inline=True)
    
    keyboard.add(OpenLink(label="Ссылка на сервис", link=youtube_link))
    keyboard.add(OpenLink(label="Смотреть", link="https://github.com/quthery/vk-youtube-bot"))
    