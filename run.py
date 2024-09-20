import asyncio
import os
from app.youtube import downloader as dw
from app.youtube import newest
from app.vk.main.handlers import download_labeler
from vkbottle import Bot,API, VideoUploader, DocMessagesUploader
from config import api, state_dispenser, labeler, user_api



labeler.load(download_labeler)

bot = Bot(
    api=api,
    labeler=labeler,
    state_dispenser=state_dispenser,
)



# @bot.on.private_message()
# async def download(message):
#     uploader = VideoUploader(user_api, generate_attachment_strings=True)

#     if not message.text.startswith("http"):
#         await message.answer("Please provide a valid video URL.")
#         return

#     # await dw.download_video(url=message.text, fsipath=f"videos/{message.from_id}")
#     title = dw.download_sync(url=message.text, fsipath=f"videos/{message.from_id}")


#     path = os.path.abspath(newest(f"{message.from_id}"))
#     print(path)



#     video = await uploader.upload(
#         file_source=path,
#         group_id=227457056,
#         owner_id=message.from_id,
#         peer_id=message.peer_id,                                 
#     )


#     await user_api.wall.post(owner_id=-227457056,from_group=True, attachments=[video], message=title)

#     await message.answer("Запосчено") 
#     os.remove(path)      

bot.run_forever()
