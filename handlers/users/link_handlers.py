from aiogram import types
from loader import dp
from pytube import YouTube
from io import BytesIO
@dp.message_handler()
async def dowload(message: types.Message):
    try:
        if message.text.startswith == 'https://www.youtube.com/' or 'https://youtube.be/':
            yt = YouTube(message.text)
            await message.answer(f"Siz <b>{yt.title}</b> \nvideoni Yuklash uchun Link yubordinggiz, "
                                 f"\nVideo yuklanish jarayonida!!!!")
        yt = YouTube(message.text)
        stream = yt.streams.get_by_itag(18)
        buffer = BytesIO()
        stream.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        await message.reply_video(video=buffer)
    except:
        pass

