# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

import sys

import PunyaAlby
from PunyaAlby import LOGS

from .Session.multisession_ import Pyrogram
from .Var import Database


def start():
    if PunyaAlby.ALBYBot:
        LOGS.info(
            f"꧁༺ ALBY-PYROBOT ༻꧂\n⚙️ Version:{PunyaAlby.__version__} [TELAH DIAKTIFKAN]"
        )


if __name__ == "__main__":
    if Database.PyroSESSION:
        Pyrogram()
        start()

if PunyaAlby.ALBYBot:
    try:
        if len(sys.argv) not in (1, 3, 4):
            PunyaAlby.ALBYBot.disconnect()
        else:
            PunyaAlby.ALBYBot.run_until_disconnected()
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
