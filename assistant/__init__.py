import os
import sys
import time
import asyncio
import pyroaddon
from pyrogram import Client
from pyrogram.errors import PeerIdInvalid

StartTime = time.time()
asst_version = "0.5.2"

if os.path.exists("config.py"):
    from config import *
else:
    from sampleconfig import *

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 8:
    print("You MUST have a python version of at least 3.8! Multiple features depend on this. Bot quitting.")
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


print("Retriving owner info")
get_user = OWNER_ID
OWNER_NAME = None
OWNER_USERNAME = None
try:
    owner = asstb.get_users(get_user)
    OWNER_NAME = owner.first_name + (owner.last_name or "")
    OWNER_USERNAME = owner.username
except PeerIdInvalid:
    print("Unable to retrive OWNER_ID")

# Some vars
SUPPORT_CHAT = 1
MUST_JOIN_CHANNEL = -1001800595118
MUST_JOIN_CHANNEL_USERNAME = "MinkxxSays"
