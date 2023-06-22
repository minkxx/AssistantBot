from pyrogram import filters
from pyrogram.types import Message

from assistant import (
    asstb,
    MUST_JOIN_CHANNEL,
    MUST_JOIN_CHANNEL_USERNAME,
    )


@asstb.on_message(filters.incoming & filters.private, group = -2)
async def check_user_in_channel(c : asstb, m :Message):
    user_id = m.from_user.id
    member_list = []
    async for member in c.get_chat_members(MUST_JOIN_CHANNEL):
        member_list.append(member.user.id)
    if user_id not in member_list:
        await m.delete()
        await c.send_message(
            chat_id = m.chat.id, 
            text= f"Join @{MUST_JOIN_CHANNEL_USERNAME} and /start again",
            )
        await m.stop_propagation()