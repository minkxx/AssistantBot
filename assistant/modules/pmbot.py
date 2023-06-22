from pyrogram import filters
from pyrogram.types import Message

from assistant import (asstb, OWNER_ID)

@asstb.on_message(filters.private & filters.incoming, group=-1)
async def pmbot(c : asstb, m : Message):
    # Filters bot commands and anything other than text
    if not m.text:
        await c.send_message(
            chat_id = m.chat.id,
            text = "**Don't send anything other than texts**",
            reply_to_message_id = m.id,
        )
    elif m.text.startswith("/"):
        return
    
    # Recives text to be sent
    if not m.from_user.id ==OWNER_ID:
        global sender_msg_id
        sender_msg_id = None

        global sender_id
        sender_id = None

        full_name = m.from_user.first_name + (m.from_user.last_name or '')

        sender_id = m.from_user.id
        sender_msg_id = m.id
        await c.send_message(
            chat_id = OWNER_ID,
            text = f"**Sender ID :** `{sender_id}`\n**Name :** {full_name}\n**Username :**@{m.from_user.username}\n\n**Message :**\n`{m.text}`\n\n#{full_name}_{m.from_user.id}",
            disable_web_page_preview = True
        )
    # Recives owner reply text and sends to user
    else:
        if m.reply_to_message:
            await c.send_message(
                chat_id = sender_id,
                text = m.text,
                reply_to_message_id = sender_msg_id,
            )
        else:
            await c.send_message(
                chat_id = m.chat.id,
                text = "**Reply to a user message instead!**",
                reply_to_message_id = m.id,
            )