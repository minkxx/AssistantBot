import requests

from pyrogram import filters
from pyrogram.types import Message

from assistant import X_RAPIDAPI_KEY, X_RAPIDAPI_HOST, asstb

__MODULE__ = "Weather"
__HELP__ = """`/weather valid_location_name`"""

headers = {"X-RapidAPI-Key": X_RAPIDAPI_KEY, "X-RapidAPI-Host": X_RAPIDAPI_HOST}


def convert_f_to_c(temp_in_fahrenheit):
    celsius = float(temp_in_fahrenheit - 32.00) * float(5.00 / 9.00)
    return round(celsius)


@asstb.on_message(filters.command("weather"))
async def weather(c: asstb, m: Message):
    cmd = m.command
    if len(cmd) != 2:
        await c.send_message(
            chat_id=m.chat.id,
            text="Wrong input provided! Please do\n`/weather valid_location_name`",
            reply_to_message_id=m.id,
        )
    else:
        location = cmd[1]
        try:
            url = f"https://open-weather13.p.rapidapi.com/city/{location}"
            response = requests.get(url, headers=headers)
            data = response.json()
            if data["cod"] == 200:
                text = f"""**Weather details of {data['name']}**
# Status : {data['weather'][0]['description']}

**# Coordinates**
Longitute : `{data['coord']['lon']}°`
Latitude : `{data['coord']['lat']}°`

**# Weather**
Temp : `{convert_f_to_c(data['main']['temp'])}°C`
Min Temp : `{convert_f_to_c(data['main']['temp_min'])}°C`
Max Temp : `{convert_f_to_c(data['main']['temp_max'])}°C`
Pressure : `{data['main']['pressure']} millibars`
Humidity : `{data['main']['humidity']} g/m³`
Wind Speed : `{data['wind']['speed']} km/h`"""

                await c.send_message(
                    chat_id=m.chat.id, text=text, reply_to_message_id=m.id
                )
            else:
                text = f"**Error** : {data['message']}"
                await c.send_message(
                    chat_id=m.chat.id, text=text, reply_to_message_id=m.id
                )

        except Exception as e:
            await c.send_message(
                chat_id=m.chat.id,
                text=f"An error occured while fetching weather details for **{location}** !!\nError : {e}",
                reply_to_message_id=m.id,
            )
