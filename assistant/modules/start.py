from pyrogram import filters
from pyrogram.types import Message
from pyroaddon.helpers import ikb

from assistant import (asstb, OWNER_USERNAME)

@asstb.on_message(filters.command("start"))
async def start_cmd(c : asstb, m : Message):
        _img = "https://graph.org/file/6d37af28a21b094079ff5.jpg"
        txt = f"Hey! {m.from_user.first_name} gald to see you here. I'm @{OWNER_USERNAME}'s personal assistant bot. You can contact him through me!\n\n/help - to get my help menu"
        keyboard = ikb([
    [("Dev", "t.me/minkxx69", "url"), ("Github", "https://github.com/minkxx", "url"), ("Repo", "https://github.com/AssistantBot", "url")],
    [("Channel", "https://t.me/MinkxxSays", "url"), ("Group", "https://t.me/BotsUnion", "url")]
])
        await c.send_photo(
            chat_id=m.chat.id,
            photo = _img,
            caption = txt,
            reply_to_message_id = m.id,
            reply_markup=keyboard,
            )
