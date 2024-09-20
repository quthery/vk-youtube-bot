import asyncio
import os
from app.youtube import downloader as dw
from app.youtube import newest

from vkbottle import Bot,API, VideoUploader, DocMessagesUploader
from config import api, state_dispenser, labeler, user_api, service_api
from app.vk.handlers import chat_labeler, admin_labeler

bot = Bot(
    api=api,
    labeler=labeler,
    state_dispenser=state_dispenser,
)


@bot.on.message()
async def download(message):
    uploader = VideoUploader(user_api, generate_attachment_strings=True)

    if not message.text.startswith("http"):
        await message.answer("Please provide a valid video URL.")
        return

    # Download the video
    await dw.download_video(url=message.text, fsipath=f"videos/{message.from_id}")

    # Get the path of the most recently downloaded video
    path = os.path.abspath(newest(f"{message.from_id}"))
    print(path)

    # Upload the video to VK


    video = await uploader.upload(
        file_source=path,
        owner_id=message.from_id,                # The user ID of the user who uploaded the video
        peer_id=message.peer_id,                  # The user ID of the user who sent the message                                    
        name="asd.mp4"
    )


    # Post the video to the wall and send it back to the user
    await user_api.wall.post(owner_id=-227457056, attachments=[video], message=path)
    await message.answer("Запосчено")

# Run the bot
bot.run_forever()
