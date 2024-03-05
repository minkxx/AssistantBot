from functools import wraps

from pyrogram.types import Message

from assistant import OWNER_ID


async def your_are_not_owner(client, m):
    await client.send_message(
        chat_id=m.chat.id,
        text="You are not owner to execute this command !!",
        reply_to_message_id=m.id,
    )


def owner_only(func):
    @wraps(func)
    def wrapper(client, message: Message, *args, **kwargs):
        if message.from_user and message.from_user.id == OWNER_ID:
            return func(client, message, *args, **kwargs)
        else:
            print(
                "Unauthorized access! This command can only be executed by the owner."
            )
            # You can customize the behavior for unauthorized access here
            # For example, you might want to send a message to the user, log the attempt, etc.
            return your_are_not_owner(client, message, *args, **kwargs)

    return wrapper
