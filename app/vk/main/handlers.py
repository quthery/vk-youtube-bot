from vkbottle import VideoUploader
from vkbottle.bot import BotLabeler, Message
from app.youtube import downloader as dw
from app.youtube import newest
from app.vk.keyboard.keyboard import keyboard as kb
from app.lib import getSize, convert_size, description
from config import user_api 
import asyncio
import time
import os


download_labeler = BotLabeler()
uploader = VideoUploader(user_api, generate_attachment_strings=True)

@download_labeler.private_message(regexp="^(https://(www\.)?youtube\.com)")                         
async def download(message: Message):

    start_time = time.time()                
    Video = await dw.download_async(url=message.text, fsipath=f"videos/{message.from_id}")

    path = os.path.abspath(newest(f"videos/{message.from_id}"))


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

    post_id = await user_api.wall.post(owner_id=-227457056,from_group=True, attachments=[video], message=msg)   

    keyboard = kb(url_hosting=Video.webpageurl, url_video=f"https://vk.com/{video}")
    await message.answer(attachment=video, message=msg, keyboard=keyboard)

    os.remove(path)         

