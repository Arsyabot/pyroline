# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••


from pyrogram import Client

from .._database._var import Database
from .classbot import Pyrobot

loop = None


if Database.PYROGRAM_SESSION:
    pyrobot = Client(
        Database.PYROGRAM_SESSION,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
else:
    pyrobot = None
if Database.PYROGRAM_SESSION2:
    pyrobot2 = Client(
        Database.PYROGRAM_SESSION2,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
else:
    pyrobot2 = None
if Database.PYROGRAM_SESSION3:
    pyrobot3 = Client(
        Database.PYROGRAM_SESSION3,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
else:
    pyrobot3 = None
if Database.PYROGRAM_SESSION4:
    pyrobot4 = Client(
        Database.PYROGRAM_SESSION4,
        api_id=Database.APP_ID,
        api_hash=Database.API_HASH,
        sleep_threshold=180,
    )
else:
    pyrobot4 = None

if Database.BOT_TOKEN:
    pyrotgbot = Pyrobot()
