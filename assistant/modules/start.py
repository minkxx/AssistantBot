from pyrogram import filters
from pyrogram.types import Message
from pyroaddon.helpers import ikb

from assistant import asstb

@asstb.on_message(filters.command("start"))
async def start_cmd(c : asstb, m : Message):
        txt = f"Hey! {m.from_user.first_name} gald to see you here. I'm @minkxx69 's personal assistant bot. You can contact him through me!"
        keyboard = ikb([
    [("Dev", "t.me/minkxx69", "url"), ("Github", "https://github.com/minkxx", "url"), ("Repo", "https://github.com/AssistantBot", "url")],
    [("Channel", "https://t.me/MinkxxSays", "url"), ("Group", "https://t.me/BotsUnion", "url")]
])
        await c.send_message(
            chat_id=m.chat.id,
            text=txt,
            reply_to_message_id = m.id,
            reply_markup=keyboard, 
            disable_web_page_preview=True,
            )
