
from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Şəxsi Qrup"
        logger_text = f"""
**ƏKBƏR MUSİC PLAY LOG**

**Qrup:** {message.chat.title} [`{message.chat.id}`]
**İsdifadəçi:** {message.from_user.mention}
**İsdifadəçi Adı:** @{message.from_user.username}
**İsdifadəçi İD:** `{message.from_user.id}`
**Qrup Link:** {chatusername}

**Sorğu:** {message.text}

**Axın Növü:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
