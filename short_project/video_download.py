import pytube
from pytube import * 
print('Hi, this is youtube video  downloader ')

url=input('enter a  video link ::')
yt=pytube.YouTube(url)
yt.streams.first().download()
print('dowloading', url)
