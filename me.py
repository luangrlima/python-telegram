#!/usr/bin/env python3
# A simple script to print some messages.
from telethon.sync import TelegramClient

import os

def get_env(name, message, cast=str):
    if name in os.environ:
        return os.environ[name]
    while True:
        value = input(message)
        try:
            return cast(value)
        except ValueError as e:
            print(e, file=sys.stderr)
            time.sleep(1)

api_id = get_env('TG_API_ID', 'Enter your API ID: ', int) 
api_hash = get_env('TG_API_HASH', 'Enter your API hash: ')
session = get_env('TG_SESSION', 'Enter your SESSION: ')

client = TelegramClient(session, api_id, api_hash)

async def main():
    me = await client.get_me()
    print(me.username,' - phone: ' ,me.phone)
with client:
    client.loop.run_until_complete(main())
