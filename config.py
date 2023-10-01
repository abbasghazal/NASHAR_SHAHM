from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID", "15179868")
APP_HASH = os.environ.get("APP_HASH", "5eed1d89e639551bd74d736037ebd4f9")
SESSION = os.environ.get("SESSION")
ha313so = TelegramClient(StringSession(SESSION), APP_ID, APP_HASH)
ha313so.start()
