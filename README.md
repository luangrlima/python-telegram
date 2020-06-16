# Python Telethon Telegram
> Code examples for using telegram with telethon.

The purpose of the codes is to demonstrate how to use python to consume the resources of the telethon.

<p align="center">
  <img  src="header.png">
</p>
## Installation

You need to download and install Python from [Python Downloads](https://www.python.org/downloads/)  if you haven’t already.

OS X & Linux:
```sh
pip3 install -U telethon --user
```

## Verification
To verify that the library is installed correctly, run the following command:

```sh
python3 -c "import telethon; print(telethon.__version__)"
```

## Development setup

```sh
git clone https://github.com/luangrlima/python-telegram.git
cd python-telegram
```

## Signing In
Before working with Telegram’s API, you need to get your own API ID and hash:

1. [Login to your Telegram](https://my.telegram.org/) account with the phone number of the developer account to use.
1. Click under API Development tools.
1. A *Create new application* window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (*App title and Short name*) can currently be changed later.
1. Click on *Create application* at the end. Remember that your **API hash is secret** and Telegram won’t let you revoke it. Don’t post it anywhere!

## Usage example

For you to use the codes, just use the python3 resource and the file name with extension. To run the code, use `python3 me.py` from the terminal.

As the following examples:
```sh
python3 me.py
python3 dialogs.py
python3 messages.py
python3 contacts.py
python3 channel.py
```

Each code will request at least three things: `api_id`, `api_hash` and `session`.

And if it is the first time or modify the `session`, he will ask for your phone (or bot token) and the code you received in your telegram.

success message: `Signed in successfully as [YOUR NAME]`

## Meta

Luan Lima – [Website][luan-website] – [E-mail][luan-email] - [Github][luan-github]

[Github - Python Telethon Telegram][luan-github-project]

## Contributing

1. Fork it (<https://github.com/luangrlima/python-telegram/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[luan-website]: https://luanlima.com.br
[luan-email]: mailto:contato@luanlima.com.br
[luan-github]: https://github.com/luangrlima
[luan-github-project]: https://github.com/luangrlima/python-telegram/