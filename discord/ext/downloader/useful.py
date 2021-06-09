import pytube
import discord
from .errors import VideoTooLong, BadLink


def youtubeDownloader(url, length):
    '''Check YouTube video length.'''
    if pytube.YouTube(url).length > length:
        return raise VideoTooLong(f'Video length was too long. Needs to be less than {length} seconds')
    else:
        if "youtu" in url:
            try:
                downloader(url)
                return discord.File("download.mp4")
            except:
                return raise BadLink('Invalid Link.')
        else:
            return raise BadLink('Invalid Link.')

def downloader(url):
    pytube.YouTube(url).streams.get_by_itag(18).download(filename="download")