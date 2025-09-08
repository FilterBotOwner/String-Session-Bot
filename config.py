import os
from typing import List

API_ID = os.environ.get("API_ID", "28568452")
API_HASH = os.environ.get("API_HASH", "8439af0a8ecc67bca4859180e7f9c8b9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "6069621485"))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002928086310"))

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "")

IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002442800721 -1002452288568").split())) # Add Multiple channel ids
