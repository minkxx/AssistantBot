import os
from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message

from assistant import (asstb)

@asstb.on_message(filters.command("whois"))
async def whois_cmd(c : asstb, m : Message):
    protext = await m.reply("__Processing...__")
    cmd = m.command
    if not m.reply_to_message and len(cmd) == 1:
        get_user = m.from_user.id
    elif len(cmd) == 1:
        get_user = m.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        # try:
        #     get_user = int(cmd[1])
        # except ValueError:
        #     await c.send_message(
        #         chat_id = m.chat.id,
        #         text = "Please provide a valid id and not a text",
        #         reply_to_message_id = m.id
        #     )
    try:
        user = await c.get_users(get_user)
    except PeerIdInvalid:
        await c.send_message(
            chat_id = m.chat.id,
            text = "Given user's id is invalid.",
            reply_to_message_id = m.id
            )
        return

    try:
        pfp = c.get_chat_photos(user.id)
        pfp_list = []
        async for photo in pfp:
            pfp_list.append(photo)
        dll = (pfp_list[0].file_id)
        x = await c.download_media(
            message = dll,
            file_name = f"{user.id}_pfp.png",
        )
    except IndexError:
        x = None
        pfp = None

    full_name = user.first_name + (user.last_name or "")
    user_id = user.id
    username = user.username
    dc_id = user.dc_id or "1"
    status = user.status or "None"
    bot = user.is_bot
    verification = user.is_verified
    scam = user.is_scam
    premium = user.is_premium

    whois_msg = f'''**[{full_name}](tg://user?id={user_id})**
• User id : `{user_id}`
• Username : @{username}
• DC : `{dc_id}`
• Status : `{status}`
• Scam : `{scam}`
• Bot : `{bot}`
• Premium : `{premium}`
• Verified : `{verification}`
'''
    if not pfp:
        await protext.delete()
        await c.send_message(
            chat_id = m.chat.id,
            text = whois_msg,
            reply_to_message_id = m.id,
            disable_web_page_preview = True,
        )
    else:
        await protext.delete()
        await c.send_photo(
            chat_id = m.chat.id,
            photo = x,
            caption = whois_msg,
            reply_to_message_id = m.id,
        )
    if x:
        os.remove(x)
    else:
        pass

@asstb.on_message(filters.command("id"))
async def id_cmd(c : asstb, m : Message):
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
        text = f"User id : `{user_id}`\nChat id : `{m.chat.id}`",
        reply_to_message_id = m.id
    )