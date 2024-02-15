import asyncio

from assistant import asstb
from pyrogram import Client, filters
from pyrogram.types import Message
from pyroaddon import listen
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid,
)


async def cancel_in_msg(msg):
    if "/cancel" in msg.text:
        await msg.reply("Cancelled the process")
        return True
    elif msg.text.startswith("/"):
        await msg.reply("Cancelled the process")
        return True
    else:
        return False


@asstb.on_message(filters.command("ssgen") & filters.private)
async def session_gen(c: asstb, m: Message):
    user_id = m.from_user.id

    API_ID = await c.ask(
        m.chat.id, "**Send your API_ID**\n/cancel - cancel current process"
    )
    if not API_ID.text.isdigit:
        await API_ID.edit("API_ID must be an integer")
    elif await cancel_in_msg(API_ID):
        return
    else:
        pass

    API_HASH = await c.ask(
        m.chat.id, "**Now send your API_HASH**\n/cancel - cancel current process"
    )
    if not API_HASH.text.isalpha:
        await API_HASH.edit("API_HASH must not be an integer")
    elif await cancel_in_msg(API_HASH):
        return
    else:
        pass

    PHONE_NUMBER = await c.ask(
        m.chat.id,
        "**Enter your phone number with country code**\n`Example : +91 9101069695`\n/cancel - cancel current process",
    )

    if not PHONE_NUMBER.text.isdigit:
        await PHONE_NUMBER.text.edit("PHONE_NUMBER must be an integer")
    elif await cancel_in_msg(PHONE_NUMBER):
        return
    else:
        pass

    codemsg = await c.send_message(m.chat.id, "__Sending OTP__")
    if not codemsg.text.isdigit:
        await codemsg.edit("OTP must be an integer")
    elif await cancel_in_msg(codemsg):
        return
    else:
        pass

    phone_number = PHONE_NUMBER.text
    api_id = int(API_ID.text)
    api_hash = API_HASH.text

    app = Client(
        name=f"{user_id}-annon", api_id=api_id, api_hash=api_hash, in_memory=True
    )

    await app.connect()
    try:
        code = await app.send_code(phone_number)
    except ApiIdInvalid:
        await codemsg.edit("API_ID and API_HASH invalid")
        return
    except PhoneNumberInvalid:
        await codemsg.edit("Phone number invalid")
        return

    try:
        await codemsg.delete()
        phone_code_msg = await c.ask(
            m.chat.id,
            "**Send OTP in `1 2 3 4 5` format**\n/cancel - cancel current process",
        )
        if await cancel_in_msg(phone_code_msg):
            return
    except TimeoutError:
        errmsg = await c.send_message(m.chat.id, "Timeout")
        return
    phone_code = phone_code_msg.text.replace(" ", "")

    try:
        await app.sign_in(phone_number, code.phone_code_hash, phone_code)
    except PhoneCodeInvalid:
        await errmsg.edit("OTP invalid")
        return
    except PhoneCodeExpired:
        await errmsg.edit("OTP expired")
        return
    except SessionPasswordNeeded:
        try:
            two_step_msg = await c.ask(
                m.chat.id,
                "**You have two step password enabled Please enter below**\n/cancel - cancel current process",
            )
            if await cancel_in_msg(two_step_msg):
                return
        except TimeoutError:
            await errmsg.edit("**Time out**")
            return
        try:
            password = two_step_msg.text
            await app.check_password(password)
        except PasswordHashInvalid:
            await errmsg.edit("**Invalid password**")
            return

    string_session = await app.export_session_string()
    await c.send_message(
        chat_id=m.chat.id,
        text=f"**Here is your session string**\n\n`{string_session}`\n\nPlease dont share with anyone!",
    )

    await app.disconnect()
