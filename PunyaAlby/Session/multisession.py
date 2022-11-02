import logging
from logging import getLogger

import pyrogram as albypyro

from .._func.startup import load_modulesPyro, plugin_collecter
from .client import *
from .pyroclient import *
from .pyroclient import pyrobot, pyrotgbot

LOGS = getLogger(__name__)
import os

from pyrogram import __version__ as pyrover

PRIVATE = int(os.environ.get("PRIVATE") or "-1001576424326")

cmdhr = os.environ.get("COMMAND_HAND_LER") or "."


def Pyrogram():
    if pyrotgbot:
        pyrotgbot.start()
        pyrotgbot.me = pyrotgbot.get_me()
        assistant_mods = plugin_collecter("./PunyaAlby/modules/assistant/")
        for mods in assistant_mods:
            try:
                load_modulesPyro(mods, assistant=True)
            except Exception as e:
                logging.error("[ASSISTANT] - Failed To Load : " + f"{mods} - {str(e)}")
    if pyrobot:
        pyrobot.start()
        pyrobot.me = pyrobot.get_me()
        pyrobot.has_a_bot = True if pyrotgbot else False
    if pyrobot2:
        pyrobot2.start()
        pyrobot2.me = pyrobot2.get_me()
        pyrobot2.has_a_bot = True if pyrotgbot else False
    if pyrobot3:
        pyrobot3.start()
        pyrobot3.me = pyrobot3.get_me()
        pyrobot3.has_a_bot = True if pyrotgbot else False
    if pyrobot4:
        pyrobot4.start()
        pyrobot.me = pyrobot4.get_me()
        pyrobot4.has_a_bot = True if pyrotgbot else False
    needed_mods = plugin_collecter("./PunyaAlby/modules/")
    for nm in needed_mods:
        try:
            load_modulesPyro(nm)
        except Exception as e:
            logging.error("[USER] - Failed To Load : " + f"{nm} - {str(e)}")
    if pyrobot:
        pyrobot.join_chat("ruangdiskusikami")
        pyrobot.join_chat("ruangprojects")
        pyrobot.send_message(
            PRIVATE, MSG_ON.format(pyrobot.me.username, pyrover, cmdhr)
        )
    if pyrobot2:
        pyrobot2.join_chat("ruangdiskusikami")
        pyrobot2.join_chat("ruangprojects")
        pyrobot2.send_message(
            PRIVATE, MSG_ON.format(pyrobot2.me.username, pyrover, cmdhr)
        )
    if pyrobot3:
        pyrobot3.join_chat("ruangdiskusikami")
        pyrobot3.join_chat("ruangprojects")
        pyrobot3.send_message(
            PRIVATE, MSG_ON.format(pyrobot3.me.username, pyrover, cmdhr)
        )
    if pyrobot4:
        pyrobot4.join_chat("ruangdiskusikami")
        pyrobot4.join_chat("ruangprojects")
        pyrobot4.send_message(
            PRIVATE, MSG_ON.format(pyrobot4.me.username, pyrover, cmdhr)
        )
    LOGS.info(f"꧁༺ ALBY-PYROBOT ༻꧂\n⚙️ PyroVersion:{pyrover} [TELAH DIAKTIFKAN]")
    albypyro.idle()
