import asyncio

from pyrogram import Client as c

API_ID = input("\nAPI_ID-nizi daxil edin:\n > ")
API_HASH = input("\nAPI_HASH-inizi daxil edin:\n > ")

print("\n\n Soruşanda Telefon nömrəsini daxil edin.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    xx = f"İŞTE SİZİN STRİNG SESSİYA, KOPYA EDİN, PAYLAŞMAYIN!!\n\n`{ss}`\n\nYARADAN ƏKBƏR"
    ok = await i.send_message("me", xx)
    print("\nİŞTE SİZİN STRİNG SESSİYA, KOPYA EDİN, PAYLAŞMAYIN!!\n")
    print(f"\n{ss}\n") 
    print("\nYARADAN ƏKBƏR\n")


asyncio.run(main())
