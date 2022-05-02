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
async def start(event):              
    if event.is_private:
       MKBot = await event.client.get_me()
       bot_id = MKBot.first_name
       bot_username = MKBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheMK = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝐌𝐊](https://t.me/MK_TheHacker3)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheMK,
                  MK_IMG,
                  caption=ownermsg, 
                  buttons=MK_Button)
       else:
            await event.client.send_file(TheMK,
                  MK_IMG,
                  caption=usermsg)
