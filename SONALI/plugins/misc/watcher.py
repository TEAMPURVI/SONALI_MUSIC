from pyrogram import filters
from pyrogram.types import Message

from SONALI import app
from SONALI.core.call import RAUSHAN

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await RAUSHAN.stop_stream_force(message.chat.id)
