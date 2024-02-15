from pytube import YouTube, Search


def songDl(song_name: str, download_output_path):
    nameInfo = Search(song_name)
    songId = x = str(nameInfo.results[0]).split("=")[-1].split(">")[0]
    ytUrl = f"https://www.youtube.com/watch?v={songId}"
    yt = YouTube(ytUrl)
    stream = yt.streams.filter(abr="128kbps")[0]
    song_path = stream.download(output_path=download_output_path)
    return rf"{song_path}".split("\\")[-1]
