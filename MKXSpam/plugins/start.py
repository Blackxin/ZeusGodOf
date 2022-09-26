import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from .. import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10, ALIVE_PIC, OWNER_ID
from MKXSpam.plugins.help import *


MK_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/fc09787e064ec4f0aec98.jpg"

MK_Button = [
        [
        Button.inline("• ᴄᴍᴅs •", data="help_back")
        ]
        ]


#USERS 


@MK1.on(events.NewMessage(outgoing=True))
@MK2.on(events.NewMessage(outgoing=True))
@MK3.on(events.NewMessage(outgoing=True))
@MK4.on(events.NewMessage(outgoing=True))
@MK5.on(events.NewMessage(outgoing=True))
@MK6.on(events.NewMessage(outgoing=True))
@MK7.on(events.NewMessage(outgoing=True))
@MK8.on(events.NewMessage(outgoing=True))
@MK9.on(events.NewMessage(outgoing=True))
@MK10.on(events.NewMessage(outgoing=True))
async def start(event):              
    if event.is_private:
       MKBot = await event.client.get_me()
       bot_id = MKBot.first_name
       bot_username = MKBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheMK = event.chat_id
       firstname = replied_user.user.first_name
       usermsg = f"**Hᴇʟʟᴏ, {firstname} ! Nɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ, Wᴇʟʟ 𝐈 ᴀᴍ {bot_id}, Aɴ 𝐏ᴏᴡᴇʀғᴜʟʟ Sᴘᴀᴍ Bᴏᴛ.** \n\n**🥀 𝐏ᴏᴡᴇʀᴇᴅ ʙʏ [Zꫀꪀꫀ᥊](https://t.me/Zenex_xD)**"
       if event.sender_id not in SUDO_USERS:
            await event.client.send_file(TheMK,
                  MK_IMG,
                  caption=usermsg, 
                  buttons=MK_Button)
