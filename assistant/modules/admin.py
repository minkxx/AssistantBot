from pyrogram import filters
from pyrogram.types import Message, ChatPrivileges
from pyrogram.enums import ChatMembersFilter

from assistant import BOT_ID, asstb
from assistant.core.decorators.permissions import owner_only

__MODULE__ = "Admin"
__HELP__ = """/promote - Promote A Member
/demote - Demote A Member
/pin - Pin A Message
/invitelink - Send Group/SuperGroup Invite Link."""

# /ban - Ban A User
# /unban - Unban A User
# /warn - Warn A User
# /rmwarns - Remove All Warning of A User
# /warns - Show Warning Of A User
# /kick - Kick A User
# /purge - Purge Messages
# /del - Delete Replied Message
# /fullpromote - Promote A Member With All Rights

async def get_admins(chat_id: int, *args, **kwargs):
    admin_list = []
    async for admin in asstb.get_chat_members(
        chat_id, filter=ChatMembersFilter.ADMINISTRATORS
    ):
        admin_list.append(admin.user.id)
    return admin_list


# Promote
@asstb.on_message(filters.command("promote") & filters.group)
@owner_only
async def promotehammer(c: asstb, m: Message):
    cmd = m.command
    admins = await get_admins(m.chat.id)
    bot = (await c.get_chat_member(m.chat.id, BOT_ID)).privileges
    if not BOT_ID in admins:
        await c.send_message(
            chat_id=m.chat.id, text="I'm not an admin here!", reply_to_message_id=m.id
        )
        return
    elif not bot.can_promote_members:
        await c.send_message(
            chat_id=m.chat.id,
            text="Promote me with add admin privileges!",
            reply_to_message_id=m.id,
        )
        return
    else:
        if not m.from_user.id in admins:
            await c.send_message(
                chat_id=m.chat.id,
                text="You aren't the boss here",
                reply_to_message_id=m.id,
            )
            return
        elif not m.reply_to_message and len(cmd) == 1:
            await c.send_message(
                chat_id=m.chat.id,
                text="I cant't promote no one\nCan I?",
                reply_to_message_id=m.id,
            )
            return
        else:
            if len(cmd) == 1:
                get_user = m.reply_to_message.from_user.id
            elif len(cmd) > 1:
                get_user = cmd[1]

            if get_user in admins:
                await c.send_message(
                    chat_id=m.chat.id,
                    text="How can I promote an admin?",
                    reply_to_message_id=m.id,
                )
                return

            await c.promote_chat_member(
                chat_id=m.chat.id,
                user_id=get_user,
                privileges=ChatPrivileges(
                    can_change_info=bot.can_change_info,
                    can_invite_users=bot.can_invite_users,
                    can_delete_messages=bot.can_delete_messages,
                    can_restrict_members=bot.can_restrict_members,
                    can_pin_messages=bot.can_pin_messages,
                    can_promote_members=bot.can_promote_members,
                    can_manage_chat=bot.can_manage_chat,
                    can_manage_video_chats=bot.can_manage_video_chats,
                ),
            )
            await c.send_message(
                chat_id=m.chat.id, text=f"Promoted!", reply_to_message_id=m.id
            )


# demote
@asstb.on_message(filters.command("demote") & filters.group)
@owner_only
async def demotehammer(c: asstb, m: Message):
    cmd = m.command
    admins = await get_admins(m.chat.id)
    bot = (await c.get_chat_member(m.chat.id, BOT_ID)).privileges
    if not BOT_ID in admins:
        await c.send_message(
            chat_id=m.chat.id, text="I'm not an admin here!", reply_to_message_id=m.id
        )
        return
    elif not bot.can_promote_members:
        await c.send_message(
            chat_id=m.chat.id,
            text="Promote me with add admin privileges!",
            reply_to_message_id=m.id,
        )
        return
    else:
        if not m.from_user.id in admins:
            await c.send_message(
                chat_id=m.chat.id,
                text="You aren't the boss here",
                reply_to_message_id=m.id,
            )
            return
        elif not m.reply_to_message and len(cmd) == 1:
            await c.send_message(
                chat_id=m.chat.id,
                text="I cant't demote no one\nCan I?",
                reply_to_message_id=m.id,
            )
            return
        else:
            if len(cmd) == 1:
                get_user = m.reply_to_message.from_user.id
            elif len(cmd) > 1:
                get_user = cmd[1]

            if get_user not in admins:
                await c.send_message(
                    chat_id=m.chat.id,
                    text="How can I demote someone who is not admin here?",
                    reply_to_message_id=m.id,
                )
                return

            await c.promote_chat_member(
                chat_id=m.chat.id,
                user_id=get_user,
                privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=False,
                    can_delete_messages=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_chat=False,
                    can_manage_video_chats=False,
                ),
            )
            await c.send_message(
                chat_id=m.chat.id, text=f"Demoted!", reply_to_message_id=m.id
            )

# pin
@asstb.on_message(filters.command("pin") & filters.group)
@owner_only
async def pinhammer(c: asstb, m: Message):
    if not m.reply_to_message:
        await c.send_message(
                chat_id=m.chat.id, text=f"What am I supposed to pin? Jesus?", reply_to_message_id=m.id
            )
    else:
        await c.pin_chat_message(
            chat_id=m.chat.id,
            message_id=m.reply_to_message.id
            )

        await m.reply_text("__pinned__ !")

# invite liink
@asstb.on_message(filters.command("invitelink") & filters.group)
@owner_only
async def invitehammer(c: asstb, m: Message):
    link = await c.export_chat_invite_link(m.chat.id)
    if link:
        await c.send_message(
                    chat_id=m.chat.id,
                    text=f"**Here's the invite link of this chat..**\n\n`{link}`",
                    reply_to_message_id=m.id,
                    disable_web_page_preview=True,
                )
    else:
        await c.send_message(
                chat_id=m.chat.id,
                text=f"Unable to get chat invite link!!",
                reply_to_message_id=m.id
            )