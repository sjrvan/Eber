
from pyrogram import filters

import config
from strings import get_command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database import autoend_off, autoend_on
from YukkiMusic.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**İstifadəsi:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "Yayımı avtomatik bitirmə aktivləşdirildi.\n\nHeç kim xəbərdarlıq mesajı ilə qulaq asmasa, bot 3 dəqiqədən sonra səsli söhbəti avtomatik tərk edəcək..."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("Yayımı avtomatik bitirmə deaktiv edilib.")
    else:
        await message.reply_text(usage)
