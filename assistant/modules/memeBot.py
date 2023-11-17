from assistant import memebot
import requests
import os
import time
import random
import asyncio

subReddit = ["dankmemes", "dankchristianmemes", ]

sent_post = []

async def meme_sender():
    async with memebot:
        memebot.send_message(-1001807331637, "Bot online !!")
        while True:
            try:
                sreddit = random.choice(subReddit)
                url = f"https://meme-api.com/gimme/{sreddit}"
                response = requests.get(url)
                data = response.json()
                img_url = data["url"]
                capt = f"Title : {data['title']}\nSubReddit : {data['subreddit']}"
                if img_url in sent_post:
                    continue
                else:
                    await memebot.send_photo(
                        -1002066337808,
                        img_url,
                        capt,
                        )
                    await asyncio.sleep(60*60)
                    sent_post.append(img_url)
            except Exception as e:
                print(e)
                break

memebot.run(meme_sender())
