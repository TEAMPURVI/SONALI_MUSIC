from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("ᴄʜᴀᴛ-ɢᴘᴛ", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="mplus HELP_Q"),InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("ᴛᴀɢ-ᴀʟʟ", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("ɢɪᴛʜᴜʙ", callback_data="mplus HELP_Github"),InlineKeyboardButton("ᴇxᴛʀᴀ", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("ᴀᴄᴛɪᴏɴ", callback_data="mplus HELP_Action"),InlineKeyboardButton("sᴇᴀʀᴄʜ", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("ғᴏɴᴛ", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("ᴄᴏᴜᴘʟᴇs", callback_data="mplus HELP_Couples"),InlineKeyboardButton("Ⓣ-ɢʀᴀᴘʜ", callback_data="mplus HELP_TG")],          
    [InlineKeyboardButton("<", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton(">", callback_data=f"managebot123 settings_back_helper"),
    ]]
