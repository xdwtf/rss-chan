import os
import logging
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageFilter
from pyrogram import Client

# Prevent unauthorised access to the bot
class OwnerFilter(MessageFilter):
    def filter(self, message):
        return bool(message.from_user.id == OWNER_ID)
owner_filter = OwnerFilter()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
LOGGER = logging.getLogger(__name__)

# Environment Variables
def getConfig(name: str):
    return os.environ[name]
load_dotenv('config.env')

try:
    TELEGRAM_API = getConfig('TELEGRAM_API')
    TELEGRAM_HASH = getConfig('TELEGRAM_HASH')
    BOT_TOKEN = getConfig('BOT_TOKEN')
    OWNER_ID = int(getConfig('OWNER_ID'))
    CHAT_ID = getConfig('CHAT_ID')
    CHATX_ID = getConfig('CHATX_ID')
    DELAY = int(getConfig('DELAY'))
    SESSION_STRING = str(getConfig('SESSION_STRING'))
    DATABASE_URL = getConfig('DATABASE_URL')
    if len(DATABASE_URL) == 0:
        raise KeyError
except KeyError as e:
    LOGGER.error("One or more env variables are missing! Exiting now.")
    exit(1)
try:
    CUSTOM_MESSAGES = getConfig('CUSTOM_MESSAGES')
except:
    pass

session_rss = None
if SESSION_STRING is not None and SESSION_STRING != "":
    session_rss = Client(SESSION_STRING, api_id=int(TELEGRAM_API), api_hash=TELEGRAM_HASH)

updater = Updater(token=BOT_TOKEN, use_context=True)
