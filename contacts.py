#!/usr/bin/env python3
# A simple script to print some messages.
from telethon.sync import TelegramClient
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest, AddContactRequest, GetContactsRequest, GetStatusesRequest, SearchRequest
import random
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
    print('--------- GetStatusesRequest')
    result = await client(GetStatusesRequest())
    for x in result:
        print(x)

    print('--------- GetContactsRequest ')
    result = await client(GetContactsRequest(
        hash=0
    ))
    for user in result.users:
        print(user.contact, ' ---- ID:', user.id, user.first_name, user.last_name, ' ---- phone: ',user.phone, ' ---- username:', user.username)

with client:
    client.loop.run_until_complete(main())