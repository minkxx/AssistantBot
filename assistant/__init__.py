import pyroaddon
from pyrogram import Client, idle

from config import (API_ID, API_HASH, BOT_TOKEN)

asstb = Client(
    name = "annon",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    )

asstb.start()
x = asstb.get_me()
print(x)
asstb.idle()


