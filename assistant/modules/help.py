from assistant import (asstb, BOT_USERNAME)
from pyrogram import filters
from pyrogram.types import Message, CallbackQuery
from pyrogram.enums import ChatType, ParseMode
from pyroaddon.helpers import ikb



@asstb.on_message(filters.command("help"))
async def help_cmd(c : asstb, m : Message):
    global main_text
    global main_keyboard
    main_text = None
    main_keyboard = None
    
    if m.chat.type != ChatType.PRIVATE:
        main_text = f"PM me for help"
        main_keyboard = ikb([
            [("PM", f"http://t.me/{BOT_USERNAME}?start=help", "url")]
        ])
        await c.send_message(
            chat_id = m.chat.id,
            text = main_text,
            reply_to_message_id = m.id,
            reply_markup = main_keyboard,
            disable_web_page_preview = True,)
    else:
        main_text = f"Hey {m.chat.first_name}, I,m a simple assistant bot more like a No-PM's bot.\nCheck buttons for help or you can seek help in Support Group\n\nGeneral commands:\n/start - starts bot\n/help - this help menu"
        main_keyboard = ikb([
            [("Alive", "alive_callback"), ("Whois", "whois_callback")]
        ])
        await c.send_message(
            chat_id = m.chat.id,
            text = main_text,
            reply_to_message_id = m.id,
            reply_markup = main_keyboard,
            disable_web_page_preview = True,)

@asstb.on_callback_query()
async def chat_query(c : asstb, qb : CallbackQuery):
    if qb.data == "alive_callback":
        text = f'''**Alive Command**

/alive - `to check stats`
/ping - `to check my speed`
'''
        keyboard = ikb([
            [("Back", "back_callback")]
        ])
        await qb.edit_message_text(text, reply_markup=keyboard)

    elif qb.data == "whois_callback":
        text = f'''**Whois Command**

To fetch given user info:
/whois `<id> or reply to target user`

To fetch user id or chat id:
/id `<user or chat username> or reply to target user`
'''
        keyboard = ikb([
            [("Back", "back_callback")]
        ])
        await qb.edit_message_text(text, reply_markup=keyboard)


    elif qb.data == "back_callback":
        await qb.edit_message_text(main_text, reply_markup=main_keyboard)
