import asyncio
import time
import os
import shutil
from datetime import datetime
from moviepy.editor import *

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

def MP4ToMP3(mp4_path:str):
    mp3_path = mp4_path.split(".")[0] + ".mp3"
    file = AudioFileClip(mp4_path)
    file.write_audiofile(mp3_path)
    file.close()
    os.remove(mp4_path)
    return mp3_path

def zip(zip_name:str, dir_path:str):
    x = shutil.make_archive(zip_name, "zip", dir_path)
    y = x.split("\\")
    path = f"{y[-2]}/{y[-1]}"
    return path