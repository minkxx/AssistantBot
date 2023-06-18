import asyncio
from pyrogram import idle
from assistant import (
    BOT_NAME,
    BOT_USERNAME,
    asstb,
)
from assistant.modules import ALL_MODULES
from config import LOG_GROUP

loop = asyncio.get_event_loop()

async def start_bot():
    for module in ALL_MODULES:
        imported_module = importlib.import_module("assistant.modules." + module)
    bot_modules = ""
    j = 1
    for i in ALL_MODULES:
        if j == 4:
            bot_modules += "|{:<15}|\n".format(i)
            j = 0
        else:
            bot_modules += "|{:<15}".format(i)
        j += 1
    print("+===============================================================+")
    print("|                         ASSISTANT BOT                         |")
    print("+===============+===============+===============+===============+")
    print(bot_modules)
    print("+===============+===============+===============+===============+")
    print(f"BOT STARTED AS {BOT_NAME}!")
    print(f"USERBOT STARTED AS {USERBOT_NAME}!")
    print("Sending online status!")
    await asstb.send_message(LOG_GROUP, "Bot started!")
    await idle()

if __name__ == "__main__":
    loop.run_until_complete(start_bot())