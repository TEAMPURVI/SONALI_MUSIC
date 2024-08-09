from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from SONALI import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text="ʙᴀᴄᴋ",
            callback_data=f"settingsback_helper",
        ),
       
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴀᴄᴛɪᴠᴇ",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="ᴀᴅᴍɪɴ",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="ᴀᴜᴛʜ",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʙʟᴏᴄᴋ",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="ʙᴏᴛ",
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text="ᴅᴇᴠ",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ɢ-ᴄᴀsᴛ",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="ᴘ-ʟɪsᴛ",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="ᴘʟᴀʏ",
                    callback_data="help_callback hb9",
                ),
            ], 
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ʙᴀᴄᴋ",
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data=f"close"),
            ],
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴏᴘᴇɴ ɪɴ ᴘʀɪᴠᴀᴛᴇ ", url=f"https://t.me/{app.username}?start=help"
            ),
        ],
    ]
    return buttons
