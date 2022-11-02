from PunyaAlby.core.decorators import alby_on_cmd as alby
from WhyzuProject.__main__ import bot


@alby(
    ["help", "helper"],
    cmd_help={
        "help": "Gets Help Menu",
        "example": "{ch}help",
    },
)
async def help(client, message):
    starkbot = await bot.get_me()
    bot_username = starkbot.username
    nice = await client.get_inline_bot_results(bot=bot_username, query="help")
    await client.send_inline_bot_result(
        message.chat.id, nice.query_id, nice.results[0].id, hide_via=True
    )
    await message.delete()
