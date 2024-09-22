from vkbottle import VideoUploader, Keyboard, KeyboardButtonColor, OpenLink
from vkbottle.bot import BotLabeler, Message
from app.youtube import downloader as dw
from app.youtube import newest
from app.vk.keyboard import keyboard as kb
from app.lib import getSize, convert_size
from config import user_api 
import time
import os


download_labeler = BotLabeler()
uploader = VideoUploader(user_api, generate_attachment_strings=True)

@download_labeler.message()
async def download(message: Message):
    if not message.text.startswith("http"):
        await message.answer("Please provide a valid video URL.")
        return
    

    start_time = time.time()
    Video = dw.download_sync(url=message.text, fsipath=f"videos/{message.from_id}") 

    path = os.path.abspath(newest(f"videos/{message.from_id}"))


    video = await uploader.upload(
        file_source=path,
        name=str(Video.title),
        description=Video.description,      
        group_id=227457056,                         
    )           


    end_time = time.time()
    elapsed_time = end_time - start_time

    msg = f"📝 {Video.fulltitle}\n\n"
    msg += f"📺 Канал {Video.uploader}\n"
    msg += f"📅 Видео загруженно {Video.upload_date}\n"
    msg += f"💿⚖️Размер файла {convert_size(getSize(path))}\n"
    msg += f"🖥️ Разрешение hello world"
    msg += f"🕒 Затрачено времени{round(elapsed_time, 2)} секунд\n"



    keyboard = Keyboard(inline=True)
    keyboard.add(OpenLink(label="Ссылка на сервис", link=Video.webpageurl))
    keyboard.add(OpenLink(label="Смотреть", link=f"https://vk.com/video-227457056_{video.id}"))



    post_id = await user_api.wall.post(owner_id=-227457056,from_group=True, attachments=[video], message=msg)

    await message.answer(attachment=f"wall-227457056_{post_id.post_id}", keyboard=keyboard)
    os.remove(path)       
