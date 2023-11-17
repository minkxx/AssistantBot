import os

# Your app id and app hash from my.telegram.org
API_ID = int(os.environ.get("API_ID", 1))
API_HASH = os.environ.get("API_HASH", None)

# Your bot token from t.me/BotFather
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

# Get your id from t.me/MissRose_bot /id
OWNER_ID = int(os.environ.get("OWNER_ID", 1))

# Add t.me/MissRose_bot to your log group and type /id to get groupid
LOG_GROUP = int(os.environ.get("LOG_GROUP", 1))

# for my personal use
MINKXX_BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
