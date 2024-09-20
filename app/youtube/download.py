import yt_dlp
import asyncio


class Downloader:
    def __init__(self):
        self.ydl_opts = {
            'format': 'bestvideo[height<=720]+best',
            'quiet': True,
            'no_warnings': True,
            'outtmpl': '%(id)s.%(ext)s',
        }
    async def download_video(self, url, fsipath: str) -> str:
        with yt_dlp.YoutubeDL({'outtmpl': fsipath + "/%(id)s.%(ext)s", 'quiet': True, }) as ydl:
            await asyncio.get_event_loop().run_in_executor(None, ydl.download, url)

        return self.ydl_opts['outtmpl']



downloader = Downloader()