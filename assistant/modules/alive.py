import platform
import time
import socket
from sys import version_info
from datetime import datetime

from pyrogram import filters, __version__
from pyrogram.types import Message

from assistant import asstb, StartTime, OWNER_NAME, asst_version
from assistant.funcs.helpers import get_readable_time


@asstb.on_message(filters.command("alive"))
async def alive_cmd(client: asstb, message: Message):
    img_ = "https://graph.org/file/6d37af28a21b094079ff5.jpg"
    my_system = platform.uname()
    python_version = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"
    uptime = get_readable_time((time.time() - StartTime))

    alive_text = f"""**{OWNER_NAME}'s Assistant Bot is alive!**

• Assistant version : `{asst_version}`
• Python version : `{python_version}`
• Pyrogram version : `{__version__}`

• System : `{my_system.system}`
• Uptime : `{uptime}`"""

    await client.send_photo(
        chat_id=message.chat.id,
        photo=img_,
        caption=alive_text,
    )


@asstb.on_message(filters.command("ping"))
async def pingme(client: asstb, message: Message):
    start = datetime.now()
    x = await client.send_message(
        chat_id=message.chat.id,
        text="__Pong!__",
        reply_to_message_id=message.id,
    )
    uptime = get_readable_time((time.time() - StartTime))
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    hostname = socket.gethostname()
    await x.edit(f"• Ping : `{m_s}ms` 🏓\n• Uptime : `{uptime}`")
