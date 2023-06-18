import pyroaddon
from pyrogram import Client

from config import (API_ID, API_HASH, BOT_TOKEN)

asstb = Client(
    name = "annon",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="assistant\modules")
    )

asstb.start()
x = asstb.get_me()
BOT_ID = x.id
BOT_NAME = x.first_name + (x.last_name or "")
BOT_USERNAME = x.username