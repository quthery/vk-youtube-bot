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
    resolution: str
    webpageurl: str
    upload_date: str
    extractor: str   

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
    
    async def download_async(self, url: str, fsipath: str) -> Video:
        
        json = await asyncio.to_thread(self._download_sync, url, fsipath)
        
        VideoInfo = Video(
            uploader=json['uploader'],
            title=json['title'],
            thumbnail=json['thumbnail'],
            description=json['description'],
            resolution=json['height'],
            webpageurl=json['webpage_url'],
            upload_date=json['upload_date'],
            fulltitle=json['fulltitle'],
            extractor=json['extractor'],
        )
        return VideoInfo

    def _download_sync(self, url: str, fsipath: str):
        with yt_dlp.YoutubeDL({'outtmpl': fsipath + "/%(id)s.%(ext)s", 'quiet': True, 'format': 'best'}) as ydl:
            return ydl.extract_info(url)



downloader = Downloader()
