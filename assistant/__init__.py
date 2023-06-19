import sys
import time
import asyncio
import pyroaddon
from pyrogram import Client
from pyrogram.errors import PeerIdInvalid

from config import (API_ID, API_HASH, BOT_TOKEN, OWNER_ID)

StartTime = time.time()

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 7:
    print("You MUST have a python version of at least 3.7! Multiple features depend on this. Bot quitting.")
    sys.exit()

asstb = Client(
    name = "annon",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    )

asstb.start()
x = asstb.get_me()
BOT_ID = x.id
BOT_NAME = x.first_name + (x.last_name or "")
BOT_USERNAME = x.username


print("Retriving owner info.")
get_user = OWNER_ID
try:
    owner = asstb.get_users(get_user)
except PeerIdInvalid:
    print("Unable to retrive OWNER_ID")

    
OWNER_NAME = owner.first_name
OWNER_USERNAME = owner.username