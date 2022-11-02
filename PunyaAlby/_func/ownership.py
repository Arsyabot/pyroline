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
                f"𝐌𝐞𝐧𝐮 𝐇𝐞𝐥𝐩 || 𝐎𝐰𝐧𝐞𝐫: {Alive}\n\n𝗖𝗿𝗲𝗮𝘁𝗲 𝗕𝗼𝘁 𝗝𝗼𝗶𝗻 @𝗿𝘂𝗮𝗻𝗴𝗱𝗶𝘀𝗸𝘂𝘀𝗶𝗸𝗮𝗺𝗶",
                alert=True,
            )

    return wrapper
