

from pytube import YouTube

link = "https://www.youtube.com/watch?v=XZfoSEVscgU"

youtube_1 = YouTube(link)

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)


#***** stream list *******
# videos = youtube_1.streams.all()
# vid = list(enumerate(videos))
# for i in vid:
# 	print(i)
# print()
# strm = int(input('enter :  '))
# videos[strm].download()
# print('successfully')

# ************ playlist ********
from pytube import Playlist

py = Playlist('https://www.youtube.com/playlist?list=PLVgEzPHodXi01j_4aADo-Wkax7x4Dz5fQ')

print(f'Downloading: {py.title}')

for video in py.videos:
	video.streams.first().download()
