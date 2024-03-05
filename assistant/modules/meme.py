import requests
from pyrogram import filters
from pyrogram.types import Message

from assistant import asstb

__MODULE__ = "Meme"
__HELP__ = """/meme - get random reddit meme
/meme (subreddit) -  get random meme from the subreddit."""


@asstb.on_message(filters.command("meme"))
async def alive_cmd(c: asstb, m: Message):
    if len(m.command) == 1:
        try:
            url = "https://meme-api.com/gimme"
            response = requests.get(url)
            data = response.json()
            subreddit = data["subreddit"]
            title = data["title"]
            post_url = data["url"]
            is_nsfw = data["nsfw"]
            ups_count = data["ups"]
            text = (
                f"Title : {title}\nSubreddit : `r/{subreddit}`\nUp Votes : {ups_count}"
            )
            if post_url.split(".")[-1] == "png" or post_url.split(".")[-1] == "jpg":
                await c.send_photo(
                    chat_id=m.chat.id,
                    photo=post_url,
                    caption=text,
                )
            elif post_url.split(".")[-1] == "gif":
                await c.send_animation(
                    chat_id=m.chat.id,
                    animation=post_url,
                    caption=text,
                )
            elif post_url.split(".")[-1] == "mp4":
                await c.send_video(
                    chat_id=m.chat.id,
                    video=post_url,
                    caption=text,
                )
            else:
                await c.send_document(
                    chat_id=m.chat.id,
                    document=post_url,
                    caption=text,
                )
        except Exception as e:
            await c.send_message(
                chat_id=m.chat.id,
                text=f"Error : {e}",
            )
    elif len(m.command) == 2:
        try:
            url = f"https://meme-api.com/gimme/{m.command[1]}"
            response = requests.get(url)
            data = response.json()
            subreddit = data["subreddit"]
            title = data["title"]
            post_url = data["url"]
            is_nsfw = data["nsfw"]
            ups_count = data["ups"]
            text = (
                f"Title : {title}\nSubreddit : `r/{subreddit}`\nUp Votes : {ups_count}"
            )
            if post_url.split(".")[-1] == "png" or post_url.split(".")[-1] == "jpg":
                await c.send_photo(
                    chat_id=m.chat.id,
                    photo=post_url,
                    caption=text,
                )
            elif post_url.split(".")[-1] == "gif":
                await c.send_animation(
                    chat_id=m.chat.id,
                    animation=post_url,
                    caption=text,
                )
            elif post_url.split(".")[-1] == "mp4":
                await c.send_video(
                    chat_id=m.chat.id,
                    video=post_url,
                    caption=text,
                )
            else:
                await c.send_document(
                    chat_id=m.chat.id,
                    document=post_url,
                    caption=text,
                )
        except Exception as e:
            await c.send_message(
                chat_id=m.chat.id,
                text=f"Error : {e}",
            )
