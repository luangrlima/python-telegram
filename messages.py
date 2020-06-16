#!/usr/bin/env python3
# A simple script to print some messages.
from telethon.sync import TelegramClient
from telethon import functions, types

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
    user = get_env('TG_USER', 'Enter your USER: ')
    message = get_env('TG_MESSAGE', 'Enter your MESSAGE: ')

    await client.send_message(user, message)

     
    message = await client.send_message(
        user,
        'This message has **bold**, `code`, __italics__ and '
        'a [nice website](https://luanlima.com.br)!',
        link_preview=False
    )
    print(message.raw_text)
    await message.reply('Cool!')

    async for message in client.iter_messages(user):
        print(message.id, message.text)

with client:
    client.loop.run_until_complete(main())
