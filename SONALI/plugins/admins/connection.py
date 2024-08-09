from pyrogram import filters 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.enums import ChatMembersFilter
from SONALI import app
from SONALI.utils.database import connect_to_chat
from SONALI.utils.decorators import AdminActual
from config import BANNED_USERS


@app.on_message(filters.command("connect") & filters.group & ~BANNED_USERS)
async def auth(client, message: Message):
    admin_ids = [ member.user.id async for member in app.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS)]
    if not message.from_user.id in admin_ids:
        return 
    user_id = message.from_user.id
    chat_id = message.chat.id
   # re = await connect_to_chat(message.from_user.id, message.chat.id)
    
    markup = InlineKeyboardMarkup([[InlineKeyboardButton("ᴄᴏɴɴᴇᴄᴛ ᴛᴏ ᴄʜᴀᴛ ", url=f"http://t.me/{app.username}?start=connect_{chat_id}")]])
    await message.reply_text("ᴛᴀᴘ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ᴛᴏ ᴛʜɪs ᴄʜᴀᴛ ɪɴ ᴘᴍ", reply_markup = markup)
