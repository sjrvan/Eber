

HELP_1 = """**<u>👮🏼‍♂️Admin Əmrləri:👮🏼‍♂️</u>**

*c* Kanal oynatmağı nəzərdə tutur.

\n**⏸ Əmr: /pause və ya /cpause**\n**📜 Açıqlama: Musiqini fasilə ver.**\n**▶️ Əmr: /resume və ya /cresume**\n**📜 Açıqlama: Dayandırılmış musiqini davam etdirin.**\n**🔇 Əmr: /mute və ya /cmute**\n**📜 Açıqlama: Musiqinin səsini söndürün.**\n**🔊 Əmr: /unmute və ya /cunmute**\n**📜 Açıqlama: Musiqinin səsini açın.**\n**⏯ Əmr: /skip və ya /cskip**\n**📜 Açıqlama: Sıradakı musiqiyə keç.**\n**⏹ Əmr: /stop və ya /cstop**\n**📜 Açıqlama: Musiqini dayandır.**\n**🔀 Əmr: /shuffle və ya /cshuffle**\n**📜 Açıqlama: Növbəyə qoyulmuş pleylisti təsadüfi qarışdırın.**\n**⏩ Əmr: /seek və ya /cseek**\n**📜 Açıqlama: İrəli Musiqini öz müddətinizə qədər axtarın.**\n**⏪ Əmr: /seekback və ya /cseekback**\n**📜 Açıqlama: Geriyə Musiqini öz müddətinə qədər axtarın.**\n**🔃 Əmr: /restart**\n**📜 Açıqlama: Yenidən başlat.**

⏯<u>**Xüsusi Skip:**</u>
\n**⏯ Əmr: /skip or /cskip [Nömrə (məsələn: 3)]**\n**📜 Açıqlama: Musiqini müəyyən edilmiş növbəli nömrəyə ötürür. Nümunə: /skip 3 musiqini üçüncü növbəli musiqiyə ötürəcək və növbədəki 1 və 2 musiqiyə məhəl qoymayacaq.**

🔂<u>**Mahnını Təkrarla:**</u>
\n**🔂 Əmr: /loop or /cloop [aktivləşdirin/deaktiv edin] və ya [Aralarındakı nömrələr 1-10]**\n**📜 Açıqlama: Aktivləşdirildikdə, bot səsli söhbətdə cari ifa olunan musiqini 1-10 dəfə çevirir. Varsayılan olaraq 10 dəfə.**

🤵‍<u>**Auth İstifadəçiləri:**</u>
\n**📜 Açıqlama: Auth İstifadəçiləri söhbətinizdə admin hüquqları olmadan admin əmrlərindən istifadə edə bilərlər.**

\n**🤵‍♂️ Əmr: /auth [İstifadəçi adı]**\n**📜 Açıqlama: Qrupun AUTH LIST-ə istifadəçi əlavə edin.**\n**🤵‍♂️ Əmr: /unauth [İstifadəçi adı]**\n**📜 Açıqlama: Qrupun AUTH LIST-dən istifadəçini silin.**\n**🤵‍♂️ Əmr: /authusers**\n**📜 Açıqlama: Qrupun AUTH SİYAHISINI yoxlayın.**"""


HELP_2 = """⏸<u>**Oynatma Əmrləri:**</u>

Available Commands = play , vplay , cplay

ForcePlay Commands = playforce , vplayforce , cplayforce

**c** stands for channel play.
**v** stands for video play.
**force** stands for force play.

/play or /vplay or /cplay  - Bot will start playing your given query on voice chat or Stream live links on voice chats.

/playforce or /vplayforce or /cplayforce -  **Force Play** stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.

/channelplay [Chat username or id] or [Disable] - Connect channel to a group and stream music on channel's voice chat from your group.


✅**<u>Botun Server mahnı siyahıları:</u>**
/playlist  - Serverlərdə Saxlanmış Pleylistinizi Yoxlayın.
/deleteplaylist - Pleylistinizdə saxlanan hər hansı musiqini silin
/play  - Serverlərdən Saxlanmış Pleylistinizi oynatmağa başlayın."""


HELP_3 = """✅<u>**Bot Əmrləri:**</u>

\n**📊 Əmr: /stats**\n**📜 Açıqlama: Qlobal Statistikanın ən yaxşı 10 musiqisini əldə edin, botun ən yaxşı 10 istifadəçisi, botda ən yaxşı 10 söhbət, söhbətdə oynanan ən yaxşı 10 və s...**\n**🔎 Əmr: /lyrics**\n**📜 Açıqlamsa: [Muiqi Adı] - Vebdə xüsusi Musiqi üçün Lirikləri axtarır.**\n**🎵 Əmr: /song**\n**📜 Açıqlama: [Musiqi Adı] və ya [YouTube Link] - YouTube-dan mp3 və ya mp4 formatlarında istənilən treki yükləyin.**\n**⏸ Əmr: /player**\n**📜 Açıqlama: İnteraktiv Oyun Paneli əldə edin.**\n**ℹ️ Əmr: **c** **\n**📜 Açıqlama: Kanalda musıc oynatmağı nəzərdə tutur.**\n**🤵‍♂️ Əmr: /queue və ya /cqueue**\n**📜 Açıqlama: Musiqi Növbə Siyahısını yoxlayın.**"""

HELP_4 = """✅<u>**Extra  Commands:**</u>
/start - Start the Music Bot.
/help  - Get Commands Helper Menu with detailed explanations of commands.
/ping- Ping the Bot and check Ram, Cpu etc stats of Bot.

✅<u>**Group Settings:**</u>
/settings - Get a complete group's settings with inline buttons

🔗 **Options in Settings:**

1️⃣ You can set **Audio Quality** you want to stream on voice chat.

2️⃣ You can set **Video Quality** you want to stream on voice chat.

3️⃣ **Auth Users**:- You can change admin commands mode from here to everyone or admins only. If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)

4️⃣ **Clean Mode:** When enabled deletes the bot's messages after 5 mins from your group to make sure your chat remains clean and good.

5️⃣ **Command Clean** : When activated, Bot will delete its executed commands (/play, /pause, /shuffle, /stop etc) immediately.

6️⃣ **Play Settings:**

/playmode - Get a complete play settings panel with buttons where you can set your group's play settings. 

<u>Options in playmode:</u>

1️⃣ **Search Mode** [Direct or Inline] - Changes your search mode while you give /play mode. 

2️⃣ **Admin Commands** [Everyone or Admins] - If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)

3️⃣ **Play Type** [Everyone or Admins] - If admins, only admins present in group can play music on voice chat."""

HELP_5 = """🔰**<u>ADD & REMOVE SUDO USERS :</u>**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

🛃**<u>HEROKU:</u>**
/usage - Dyno Usage.

🌐**<u>CONFIG VARS:</u>**
/get_var - Get a config var from Heroku or .env.
/del_var - Delete any var on Heroku or .env.
/set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

🤖**<u>BOT COMMANDS:</u>**
/reboot - Reboot your Bot. 
/update - Update Bot.
/speedtest - Check server speeds
/maintenance [enable / disable] 
/logger [enable / disable] - Bot logs the searched queries in logger group.
/get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
/autoend [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.

📈**<u>STATS COMMANDS:</u>**
/activevoice - Check active voice chats on bot.
/activevideo - Check active video calls on bot.
/stats - Check Bots Stats

⚠️**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat - Check all blacklisted chats.

👤**<u>BLOCKED FUNCTION:</u>**
/block [Username or Reply to a user] - Prevents a user from using bot commands.
/unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
/blockedusers - Check blocked Users Lists

👤**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
/ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
/gbannedusers - Check Gbanned Users Lists

🎥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
/videomode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.

⚡️**<u>PRIVATE BOT FUNCTION:</u>**
/authorize [CHAT_ID] - Allow a chat for using your bot.
/unauthorize [CHAT_ID] - Disallow a chat from using your bot.
/authorized - Check all allowed chats of your bot.

🌐**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.

<u>options for broadcast:</u>
**-pin** : This will pin your message 
**-pinloud** : This will pin your message with loud notification
**-user** : This will broadcast your message to the users who have started your bot.
**-assistant** : This will broadcast your message from assistant account of your bot.
**-nobot** : This will force your bot to not broadcast message

**Example:** `/broadcast -user -assistant -pin Hello Testing`

"""
