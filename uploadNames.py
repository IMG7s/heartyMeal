import config
from pyrogram import Client

api_ID = config.api_ID
api_HASH = config.api_HASH

about = ''

app = Client(name="my_account", api_id=api_ID, api_hash=api_HASH)
