from pyrogram import filters
from pyrogram.types import Message
from assistant import OWNER_ID


async def only_owner(_, m: Message):
    return bool(m.from_user.id == OWNER_ID)

async def not_owner(_, m: Message):
    return bool(m.from_user.id != OWNER_ID)


owner = filters.create(only_owner)
no_owner = filters.create(not_owner)
