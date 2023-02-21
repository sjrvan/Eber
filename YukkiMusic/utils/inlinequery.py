

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Yayımı dayandırın.",
            description=f"Qrup daxilində cari oyunu dayandırın.",
            thumb_url="https://telegra.ph/file/c0a1c789def7b93f13745.png",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Yayımı davam etdirin.",
            description=f"Qrup daxilində davam edən musiqini davam etdirin.",
            thumb_url="https://telegra.ph/file/02d1b7f967ca11404455a.png",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Yayım səsini söndürün.",
            description=f"Qrup daxilində davam edən musiqini susdurun.",
            thumb_url="https://telegra.ph/file/66516f2976cb6d87e20f9.png",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="Yayım səsini aç.",
            description=f"Qrup daxilində davam edən musiqinin səsini açın.",
            thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="Yayımı dəyiş.",
            description=f"Növbəti trekə keçin. | Xüsusi trek nömrəsi üçün: /skip [sıra nömrəsi] ",
            thumb_url="https://telegra.ph/file/98b88e52bc625903c7a2f.png",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="Yayımı söndür.",
            description="Qrup daxilində davam edən musiqini söndürün.",
            thumb_url="https://telegra.ph/file/d2eb03211baaba8838cc4.png",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="Musiqini qarışdır.",
            description="Növbəyə qoyulmuş musiqi siyahısını qarışdırın.",
            thumb_url="https://telegra.ph/file/7f6aac5c6e27d41a4a269.png",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Yayımı axtarın.",
            description="Müəyyən bir müddətə davam edən axını axtarın.",
            thumb_url="https://telegra.ph/file/cd25ec6f046aa8003cfee.png",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="Yayımı təkrarla.",
            description="Cari ifa olunan musiqini təkrərlayın. | İstifadəsi: /loop [enable|disable]",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
