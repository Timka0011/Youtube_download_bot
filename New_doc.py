import pytube
from pytube import YouTube
from io import BytesIO

yt = YouTube('https://www.youtube.com/watch?v=CSl6r8VScc0&list=RDCSl6r8VScc0&start_radio=1')

link = 'https://www.youtube.com/watch?v=YT5qnF7rHsU'
buffer = BytesIO()
stream = yt.streams.get_by_itag(22)
stream.stream_to_buffer(buffer=buffer)
buffer.seek(0)



print(buffer.__sizeof__())



