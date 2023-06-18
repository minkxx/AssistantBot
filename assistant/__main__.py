import asyncio
from pyrogram import idle
from assistant import (
    BOT_NAME,
    BOT_USERNAME,
    asstb,
)
from config import LOG_GROUP

loop = asyncio.get_event_loop()

async def start_bot():
    print("Sending online status!")
    await asstb.send_message(LOG_GROUP, "Bot started!")
    await idle()

if __name__ == "__main__":
    loop.run_until_complete(start_bot())