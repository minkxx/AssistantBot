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
        path = songDl(songName, "songs/")
        send_path = MP4ToMP3(path)
        await client.send_audio(
            chat_id = message.chat.id,
            audio = send_path,
        )
    elif ("album" in (url.split("/"))) and (sClient.validUrl(url)):
        albumName, albumSongs = sClient.getAlbum(url)
        dir_path =  f"songs/{albumName}/"
        for i in albumSongs:
            path = songDl(i, dir_path)
            MP4ToMP3(path)
        zip(albumName, dir_path)
    elif ("playlist" in (url.split("/")))and (sClient.validUrl(url)):
        playlistName, playlistSongs = sClient.getPlaylist(url)
        dir_path =  f"songs/{playlistName}/"
        for j in playlistSongs:
            path = songDl(j, dir_path)
            MP4ToMP3(path)
        zip(playlistName, dir_path)
    else:
        print("Not a spotify link!")