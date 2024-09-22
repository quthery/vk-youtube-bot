from vkbottle import VideoUploader
from vkbottle.bot import BotLabeler, Message
from app.youtube import downloader as dw
from app.youtube import newest
from app.lib import getSize, convert_size
from config import user_api 
import asyncio
import time
import os


download_labeler = BotLabeler()
uploader = VideoUploader(user_api, generate_attachment_strings=True)

@download_labeler.message()
async def download(message: Message):
    if not message.text.startswith("http"):
        await message.answer("Please provide a valid video URL.")
        return
    
    await message.answer("⌛")                      


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
    msg += f"⚖️ Размер файла {convert_size(getSize(path))}\n"
    msg += f"🕒 Затрачено времени{round(elapsed_time, 2)} секунд\n"

    post_id = await user_api.wall.post(owner_id=-227457056,from_group=True, attachments=[video], message=msg)   
    # await user_api.messages.delete(peer_id=message.peer_id, cmid=message_answe.message_id, delete_for_all=True, group_id=227457056)
    await message.answer(attachment=f"wall-227457056_{post_id.post_id}")

    os.remove(path)       