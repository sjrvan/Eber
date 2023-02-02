
import sys

from pyrogram import Client
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class YukkiBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot")
        super().__init__(
            "Əkbər Music Bot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "Music Bot Başlat"
            )
        except:
            LOGGER(__name__).error(
                "Bot qrupa daxil ola bilmədi. Botunuzu log kanalınıza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun!"
            )
            sys.exit()
        if config.SET_CMDS == str(True):
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("ping", "Botun aktiv və ya passiv olduğunu yoxlayın."),
                        BotCommand("play", "Tələb olunan mahnını ifa etməyə başlayır"),
                        BotCommand("skip", "Növbədə olan növbəti mahnıya keçir."),
                        BotCommand("pause", "Hal hazırda ifa olunan mahnını dayandırın."),
                        BotCommand("resume", "Dayandırılmış mahnını davam etdirin."),
                        BotCommand("end", "Növbəni təmizləyin və səsli söhbəti tərk edin."),
                        BotCommand("shuffle", "Növbəyə qoyulmuş pleylisti təsadüfi qarışdırır."),
                        BotCommand("playmode", "Söhbətiniz üçün standart oyun rejimini dəyişməyə imkan verir."),
                        BotCommand("settings", "Söhbətiniz üçün musiqi botunun parametrlərini açın.")
                        ]
                    )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "Zəhmət olmasa Botu Log Qrupunda Admin kimi tanıtın"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"Ekber Music Bot kimi başladı {self.name}")
