import os.path

from config import labeler, api
from vkbottle import VideoUploader
from app.youtube import downloader as dw
from app.youtube import newest


upload = VideoUploader(api)

# @labeler.message()
# async def download(message):
#     await dw.download_video(url=message.text, fsipath=str(message.from_id))
#     path = os.path.abspath(newest(f"{message.from_id}"))
#     print(path)
#     video = await upload.upload(
#         file_source=path,
#         peer_id=message.peer_id,
#     )
#     await api.wall.post(owner_id=621969975, attachment=video)
#     await message.answer(attachment=video)


