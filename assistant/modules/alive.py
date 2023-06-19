import platform
import time
from sys import version_info
from pyrogram import filters, __version__
from pyrogram.types import Message

from assistant import (asstb, StartTime, OWNER_NAME)
from assistant.funcs.helpers import get_readable_time


@asstb.on_message(filters.command("alive"))
async def alive_cmd(client : asstb, message : Message):
    await message.delete()
    img_ = "https://graph.org/file/39c9ff82c41eeed2c0ae1.mp4"
    my_system = platform.uname()
    python_version = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"   
    uptime = get_readable_time((time.time() - StartTime))
    
    alive_text = f'''**{OWNER_NAME}'s Assistant Bot is alive!**

•Assistant version : `0.0.1`
•Python version : `{python_version}`
•Pyrogram version : `{__version__}`

•System : `{my_system.system}`
•Uptime : `{uptime}`'''

    if message.reply_to_message:
        await client.send_video(
            chat_id = message.chat.id,
            video = img_,
            caption=alive_text,
            reply_to_message_id=message.reply_to_message.message_id,
        )
    else:
        await client.send_video(
            chat_id = message.chat.id,
            video = img_,
            caption=alive_text)
