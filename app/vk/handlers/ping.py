from config import labeler, api
from vkbottle import VideoUploader
from app.youtube import downloader as dw
from app.youtube import downloaded_file


upload = VideoUploader(api)

@labeler.private_message()
async def download(message):
    await dw.download_video(url=message.text, fsipath=str(message.from_id))
    path = downloaded_file(str(message.text))
    print(str(message.from_id))
    video = await upload.upload(
        file_source=path[0],
        group_id=227457056,
        peer_id=message.peer_id,
    )
    await message.answer(attachment=video)


