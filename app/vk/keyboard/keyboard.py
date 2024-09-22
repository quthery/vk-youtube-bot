from vkbottle import Keyboard, KeyboardButtonColor, OpenLink, Text



def keyboard(url_hosting: str, url_video: str):
    keyboard = Keyboard(one_time=False, inline=True)
    keyboard.add(OpenLink(link=url_hosting, label="🌐YouTube"))
    keyboard.add(OpenLink(link=url_video, label="🔗 Смотреть"))
    keyboard.row()
    keyboard.add(OpenLink(link="https://github.com/quthery", label="📺 Автор"))
    keyboard.add(Text("📁 Отправить файл"), color=KeyboardButtonColor.PRIMARY)
    
    return keyboard.get_json()
    


# ...
Keyboard_kb = (
    Keyboard(one_time=False, inline=True)
    .add(Text("Кнопка 1"), color=KeyboardButtonColor.POSITIVE)
    .row()
    .add(Text("Кнопка 2"))
    .add(Text("Кнопка 3", payload={"command": 3}))
).get_json()




        

    
