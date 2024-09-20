import yt_dlp
import asyncio
from dataclasses import dataclass


@dataclass
class Video:
    uploader: str
    title: str
    description: str
    fulltitle: str
    thumbnail: str
    webpageurl: str
    upload_date: str
    extrator: str   

class Downloader:
    def __init__(self):
        self.ydl_opts = {
            'format': 'best',
            'quiet': True,
            'no_warnings': True,
            'outtmpl': 'videos/%(id)s.%(ext)s',
        }
    async def download_video(self, url, fsipath: str) -> str:
        with yt_dlp.YoutubeDL({'outtmpl': fsipath + "/%(id)s.%(ext)s", 'quiet': True, }) as ydl:
            await asyncio.get_event_loop().run_in_executor(None, ydl.download, url)

        return self.ydl_opts['outtmpl']
    
    def download_sync(self, url : str, fsipath: str) -> Video:
        with yt_dlp.YoutubeDL({'outtmpl': fsipath + "/%(id)s.%(ext)s", 'quiet': True, 'format': 'best'}) as ydl:
            json = ydl.extract_info(url)
            VideoInfo = Video(
                uploader=json['uploader'],
                title=json['title'],
                thumbnail=json['thumbnail'],
                description=json['description'],
                webpageurl=json['webpage_url'],
                upload_date=json['upload_date'],
                fulltitle=json['fulltitle'],
                extrator=json['extractor'],
            ) 
            return VideoInfo


downloader = Downloader()