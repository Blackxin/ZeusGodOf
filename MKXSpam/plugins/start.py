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


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(e):              
    if e.chat_id is e sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[Zꫀꪀꫀ᥊ 🇮🇳](tg://user?id={2102783671})"
        sudo_user = ""
        if e.sender_id in MY_USERS:
            sudo_user = "True"
        else:
            sudo_user = "False"
        ON_START = f"""
Hᴇʟʟᴏ, {mention} ! Nɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ,

Wᴇʟʟ 𝐈 ᴀᴍ Aɴ 𝐏ᴏᴡᴇʀғᴜʟʟ Sᴘᴀᴍ Bᴏᴛ. 

My master ~> {myOwner}
Sudo user ~> {sudo_user}

𝐏ᴏᴡᴇʀᴇᴅ ʙʏ {creator}

© @zenex_xD
❅──────✧──────❅
"""
        await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=ON_START, buttons=data)
       
