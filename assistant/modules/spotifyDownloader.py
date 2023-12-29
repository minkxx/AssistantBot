import os
from pyrogram import filters
from pyrogram.types import Message
from assistant import asstb, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

from assistant.funcs.helpers import MP4ToMP3, zip
from assistant.funcs.spotify import spotiSearch
from assistant.funcs.youtube import songDl

sClient = spotiSearch(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

@asstb.on_message(filters.command("spotify"))
async def spotify_downloader(client : asstb, message : Message):
    cmd = message.command
    if len(cmd) < 2:
        await client.send_message(
            chat_id = message.chat.id,
            text = "Provide me a spotify url to download.",
            reply_to_message_id = message.id)
    else:
        url = cmd[1]

    if ("track" in (url.split("/"))) and (sClient.validUrl(url)):
        songName = sClient.getTrack(url)
        y = await client.send_message(
            chat_id = message.chat.id,
            text = f"Downloading {songName} ...",
            reply_to_message_id = message.id
        )
        path = songDl(songName, "songs/")
        await y.edit_text("Converting to mp3...")
        send_path = MP4ToMP3(path)
        await y.delete()
        await client.send_audio(
            chat_id = message.chat.id,
            audio = send_path,
        )
        os.remove(send_path)
    elif ("album" in (url.split("/"))) and (sClient.validUrl(url)):
        albumName, albumSongs = sClient.getAlbum(url)
        dir_path =  f"songs/{albumName}/"
        for i in albumSongs:
            y = await client.send_message(
            chat_id = message.chat.id,
            text = f"Downloading {i} ...",
            reply_to_message_id = message.id
            )
            path = songDl(i, dir_path)
            await y.edit_text("Converting to mp3...")
            MP4ToMP3(path)
            await y.delete()
        send_path = zip(albumName, dir_path)
        z = await client.send_message(
            chat_id = message.chat.id,
            text = f"Sending zip file...",
            reply_to_message_id = message.id
            )
        await client.send_document(
            chat_id = message.chat.id,
            document = send_path,
        )
        await z.delete()
        os.remove(dir_path)
        os.remove(send_path)
    elif ("playlist" in (url.split("/")))and (sClient.validUrl(url)):
        playlistName, playlistSongs = sClient.getPlaylist(url)
        dir_path =  f"songs/{playlistName}/"
        for j in playlistSongs:
            y = await client.send_message(
            chat_id = message.chat.id,
            text = f"Downloading {j} ...",
            reply_to_message_id = message.id
            )
            path = songDl(j, dir_path)
            await y.edit_text("Converting to mp3...")
            MP4ToMP3(path)
            await y.delete()
        send_path = zip(playlistName, dir_path)
        z = await client.send_message(
            chat_id = message.chat.id,
            text = f"Sending zip file...",
            reply_to_message_id = message.id
            )
        await client.send_document(
            chat_id = message.chat.id,
            document = send_path,
        )
        await z.delete()
        os.remove(dir_path)
        os.remove(send_path)
    else:
        await client.send_message(
            chat_id = message.chat.id,
            text = "Send me a valid spotify link.",
            reply_to_message_id = message.id)

@asstb.on_message(filters.command("spotify_dls_clear"))
async def spotify_downloader(client : asstb, message : Message):
    z = await client.send_message(message.chat.id, "Clearing downloads...")
    os.remove
    await z.delete()