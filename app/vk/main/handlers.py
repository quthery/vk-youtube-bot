from vkbottle import VideoUploader
from vkbottle.bot import BotLabeler, Message
from app.youtube import downloader as dw
from app.youtube import newest
from app.vk.keyboard.keyboard import keyboard as kb
from app.lib import getSize, convert_size, description
from config import user_api 
import random
import time
import os


download_labeler = BotLabeler()
uploader = VideoUploader(user_api, generate_attachment_strings=True)

@download_labeler.private_message(regexp="^(https://(www\.)?youtube\.com)")                         
async def download_youtube(message: Message):

    start_time = time.time()      
    fsipath = f"videos/{message.from_id}/{random.randint(0, 999999)}"
    Video = await dw.download_async(url=message.text, fsipath=fsipath)

    path = os.path.abspath(newest(fsipath))


    description_for_video = description(description=Video.description, video_url=Video.webpageurl, uploader=Video.uploader)

    video = await uploader.upload(
        file_source=path,
        name=str(Video.title),                          
        description=description_for_video,      
        group_id=227457056,                         
    )           

    end_time = time.time()
    elapsed_time = end_time - start_time

    msg = f"📝 {Video.fulltitle}\n\n"
    msg += f"📺 Канал {Video.uploader}\n"
    msg += f"📅 Видео загруженно {Video.upload_date}\n"
    msg += f"⚖️ Размер файла {convert_size(getSize(path))}\n"
    msg += f"🕒 Затрачено времени {round(elapsed_time, 2)} секунд\n"


    keyboard = kb(url_hosting=Video.webpageurl, url_video=f"https://vk.com/{video}")
    await message.answer(attachment=video, message=msg, keyboard=keyboard)

    os.remove(path)         


@download_labeler.private_message(regexp="^https://(www\.)?dzen\.ru")                         
async def download_dzen(message: Message):

    start_time = time.time()                
    Video = await dw.download_async(url=message.text, fsipath=f"videos/{message.from_id}")

    path = os.path.abspath(newest(f"videos/{message.from_id}/{random.randint(0, 999999)}"))


    description_for_video = description(description=Video.description, video_url=Video.webpageurl, uploader=Video.uploader)

    video = await uploader.upload(
        file_source=path,
        name=str(Video.title),                          
        description=description_for_video,      
        group_id=227457056,                         
    )           

    end_time = time.time()
    elapsed_time = end_time - start_time

    msg = f"📝 {Video.fulltitle}\n\n"
    msg += f"📺 Канал {Video.uploader}\n"
    msg += f"📅 Видео загруженно {Video.upload_date}\n"
    msg += f"⚖️ Размер файла {convert_size(getSize(path))}\n"
    msg += f"🕒 Затрачено времени {round(elapsed_time, 2)} секунд\n"


    keyboard = kb(url_hosting=Video.webpageurl, url_video=f"https://vk.com/{video}")
    await message.answer(attachment=video, message=msg, keyboard=keyboard)

    os.remove(path)         

