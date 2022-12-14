import asyncio

from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import CallbackQuery

from ..Var import Config

Alive = Config.ALIVE_NAME
DEVBY = [1441342342, 5089916692, 2014359828, 1337194042]


def check_owner(func):
    async def wrapper(c_q: CallbackQuery):
        if c_q.query.user_id and (
            c_q.query.user_id == Config.OWNER_ID
            or c_q.query.user_id in Config.SUDO_USERS
        ):
            try:
                await func(c_q)
            except FloodWait as e:
                await asyncio.sleep(e.seconds + 5)
            except MessageNotModified:
                pass
        else:
            await c_q.answer(
                f"ššš§š® ššš„š© || šš°š§šš«: {Alive}\n\nššæš²š®šš² šš¼š šš¼š¶š» @šæšš®š»š“š±š¶ššøššš¶šøš®šŗš¶",
                alert=True,
            )

    return wrapper
