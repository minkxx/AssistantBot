from pyrogram import filters
from assistant import (asstb)
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message

@asstb.on_message(filters.command("whois"))
async def who_is(c : asstb, m : Message):
    cmd = m.command
    if not m.reply_to_message and len(cmd) == 1:
        get_user = m.from_user.id
    elif len(cmd) == 1:
        get_user = m.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            await c.send_message(
                chat_id = m.chat.id,
                text = "Please provide a valid id and not a text",
                reply_to_message_id = m.id
            )
    try:
        user = await c.get_users(get_user)
    except PeerIdInvalid:
        await c.send_message(
                chat_id = m.chat.id,
                text = "Given user's id is invalid.",
                reply_to_message_id = m.id
            )
        return
    full_name = user.first_name + (user.last_name or "")
    user_id = user.id
    username = user.username
    dc_id = user.dc_id or "1"
    status = user.status or "None"
    bot = user.is_bot
    verification = user.is_verified
    contact = user.is_contact
    scam = user.is_scam

    whois_msg = f'''**[{full_name}](tg://user?id={user_id})**
• User id : `{user_id}`
• Username : `@{username}`
• DC : `{dc_id}`
• Status : `{status}`
• Is scam : `{scam}`
• Is bot : `{bot}`
• Is verified : `{verification}`
• Is contact : `{contact}`
'''

    await c.send_message(
        chat_id = m.chat.id,
        text = whois_msg,
        reply_to_message_id = m.id,
        disable_web_page_preview = True,
    )

@asstb.on_message(filters.command("id"))
async def who_is(c : asstb, m : Message):
    cmd = m.command
    if not m.reply_to_message and len(cmd) == 1:
        get_user = m.from_user.id
    elif len(cmd) == 1:
        get_user = m.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
    try:
        user = await c.get_users(get_user)
    except PeerIdInvalid:
        await c.send_message(
                chat_id = m.chat.id,
                text = "Given user's id is invalid.",
                reply_to_message_id = m.id
            )
        return

    user_id = user.id

    await c.send_message(
        chat_id = m.chat.id,
        text = f"User id : `{user_id}`\nChat id : {m.chat.id}",
        reply_to_message_id = m.id
    )