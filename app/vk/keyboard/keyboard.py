from vkbottle import Keyboard, KeyboardButtonColor, OpenLink, Text



def keyboard(url_hosting: str, url_video: str):
    keyboard = Keyboard(one_time=False, inline=True)
    keyboard.add(OpenLink(link=url_hosting, label="🌐YouTube"))
    keyboard.add(OpenLink(link=url_video, label="🔗 Смотреть"))
    keyboard.row()
    keyboard.add(OpenLink(link="https://github.com/quthery", label="📺 Автор"))
    keyboard.add(Text("📁 Отправить файл"), color=KeyboardButtonColor.PRIMARY)
    
    return keyboard.get_json()
    

start_keyboard = (
    Keyboard(one_time=True, inline=False)
    .add(Text("Профиль 🪪"), color=KeyboardButtonColor.POSITIVE)
    .row()
    .add(Text("Статистика 📊"))
    .add(Text("FAQ 🤷"))
).get_json()




        

    
