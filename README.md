<h1 align="center">
  <b>Assistant Bot</b>
</h1>

<p align="center">
  <b>Telegram assistant bot for you. More like No-PM's Bot.</b>
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/AssistantBot-v1.0-crimson" alt="AssistantBot version"></a>
  <a href="https://github.com/minkxx/AssistantBot/stargazers"><img src="https://img.shields.io/github/stars/minkxx/AssistantBot?style=flat-square&color=yellow" alt="Stars"></a>
  <a href="https://github.com/minkxx/AssistantBot/fork"><img src="https://img.shields.io/github/forks/minkxx/AssistantBot?style=flat-square&color=orange" alt="Forks"></a>
  <a href="https://github.com/minkxx/AssistantBot/"><img src="https://img.shields.io/github/repo-size/minkxx/AssistantBot?style=flat-square&color=green" alt="Repo Size"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-v3.11.4-blue" alt="Python"></a>
  <a href="https://github.com/minkxx/AssistantBot/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-GPL-blue" alt="License"></a>
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
</p>

## Features

- **Automated Responses:** Automatically respond to messages based on predefined rules.
- **No-PM's Mode:** Block private messages and notify the user.
- **Logging:** Log all interactions to a specified group for review.
- **Weather Updates:** Fetch weather updates using RapidAPI.
- **Custom Commands:** Add custom commands to extend bot functionality.

## Installation

Follow these steps to install and run Assistant Bot:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/minkxx/AssistantBot.git
   ```

2. **Navigate to the cloned folder:**
   ```sh
   cd AssistantBot
   ```

3. **Obtain the necessary variables** (see [Necessary Variables](#necessary-variables)).

4. **Create a `config.py` file** and store the necessary variables:
   ```python
   # config.py
   API_ID = 'your_api_id'
   API_HASH = 'your_api_hash'
   BOT_TOKEN = 'your_bot_token'
   OWNER_ID = 'your_owner_id'
   LOG_GROUP = 'your_log_group'
   X_RAPIDAPI_KEY = 'your_rapidapi_key'
   X_RAPIDAPI_HOST = 'your_rapidapi_host'
   ```

5. **Install the required packages:**
   ```sh
   pip install -U -r requirements.txt
   ```

6. **Run the bot:**
   ```sh
   python -m assistant
   ```

## Necessary Variables

You will need to set the following variables in your `config.py` file:

- `API_ID` - Get it from [my.telegram.org](https://my.telegram.org/)
- `API_HASH` - Get it from [my.telegram.org](https://my.telegram.org/)
- `BOT_TOKEN` - Get it from [BotFather](https://t.me/BotFather)
- `OWNER_ID` - Get it from [MissRose_bot](https://t.me/MissRose_bot)
- `LOG_GROUP` - Get it from [MissRose_bot](https://t.me/MissRose_bot)
- `X_RAPIDAPI_KEY` - Get it from [RapidAPI](https://rapidapi.com/worldapi/api/open-weather13/)
- `X_RAPIDAPI_HOST` - Get it from [RapidAPI](https://rapidapi.com/worldapi/api/open-weather13/)


## License

This project is licensed under the GPL License - see the [LICENSE](https://github.com/minkxx/AssistantBot/blob/master/LICENSE) file for details.

