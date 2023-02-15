
import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from YukkiMusic import LOGGER, app, userbot
from YukkiMusic.core.call import Yukki
from YukkiMusic.plugins import ALL_MODULES
from YukkiMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Əkbər Music Bot").error(
            "Asistan Müəyyən edilməyib!.. Prosesdən Çıxış."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Əkbər Music Bot").warning(
            "Heç bir Spotify Versiyası müəyyən edilməyib. Botunuz spotify sorğularını səsləndirə bilməyəcək."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("YukkiMusic.plugins" + all_module)
    LOGGER("Yukkimusic.plugins").info(
        "Uğurla Import edilmiş Modullar... "
    )
    await userbot.start()
    await Yukki.start()
    try:
        await Yukki.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Əkbər Music Bot").error(
            "[ERROR] - \n\nZəhmət olmasa Logger Qrupunuzun Səsli Zəngini yandırın. Günlük qrupunuzda səsli zəngi heç vaxt bağlamadığınızdan/bitirmədiyinizdən əmin olun."
        )
        sys.exit()
    except:
        pass
    await Yukki.decorators()
    LOGGER("Əkbər Music Bot").info("Əkbər Musiqi Botu Uğurla Başladı...")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Əkbər Music Bot").info("Əkbər Musiqi Botunu dayandırın! Əlvida")
