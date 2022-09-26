from MKXSpam import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10, SUDO_USERS
from telethon import events, Button
from MKXSpam import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/a2beccc714b5f011dd42d.jpg"

MK_Help = "__Click On Below Buttons for help__"


@MK1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@MK10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=MK_Help,
                                  buttons=[
           [
            Button.inline("• 𝐒ᴘᴀᴍ •", data="spam"),
            Button.inline("• 𝐑ᴀɪᴅ •", data="raid"),
           ],
           [
            Button.inline("• 𝐄xᴛʀᴀ •", data="extra"),
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**

**Userbot**: Userbot Cmds
command:
i) {hl}ping
ii) {hl}alive
iii) {hl}restart
iv) {hl}addsudo <reply to user> : Owner Cmd

**Echo**: 𝐓ᴏ Aᴄᴛɪᴠᴇ Eᴄʜᴏ ᴏɴ ᴀɴʏ ᴜsᴇʀ
Cᴏᴍᴍᴀɴᴅs :
i) {hl}addecho <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>
ii) {hl}rmecho <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

**Leave**: To Leave Group/channel
command:
i) {hl}leave <group/chat id>
ii) {hl}leave : Type in the Group bot will auto leave that group

**Packspam**: 𝐒ᴛɪᴄᴋᴇʀ Pᴀᴄᴋ Sᴘᴀᴍ
i) {hl}packspam (replying to any sticker)

**© @ZeNeX_xD**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**Raid:** Activates ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ ғᴏʀ ɢɪᴠᴇɴ  Rᴀɴɢᴇ.
command:
i) {hl}raid <count> <username>
ii) {hl}raid <count> <ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ>

**Delayraid**: Aᴄᴛɪᴠᴀᴛᴇs raid on any individual user for given range.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>

**Replyraid:** Activates Rᴇᴘʟʏ Rᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ!!
command:
i) {hl}replyraid <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>
ii) {hl}dreplyraid <ᴜsᴇʀɴᴀᴍᴇ>

**Dreplyraid:** Deactivates rᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ!!
command:
i) {hl}dreplyraid <ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴜsᴇʀ>
ii) {hl}dreplyraid <ᴜsᴇʀɴᴀᴍᴇ>


**© @ZeNeX_xD**
"""

spam_msg = f"""
**Help Spam Cmds**

**Spam**: Spams a message for given counter(<= 100).
command:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>

**Bigspam**: Spams a message for given counter.
command:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>

**Delayspam**: Delay spam a text for given counter after given time.
command:
i) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay> <count> <replying any message>

**Pornspam**: Pornography Spam.
command:
i) {hl}pornspam <count>

**Hang**: Spams hanging message for given counter.
command:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @MAGNESIUM_XD**
"""                     
           
           
@MK1.on(events.CallbackQuery(pattern=r"help_back"))
@MK2.on(events.CallbackQuery(pattern=r"help_back"))
@MK3.on(events.CallbackQuery(pattern=r"help_back"))
@MK4.on(events.CallbackQuery(pattern=r"help_back"))
@MK5.on(events.CallbackQuery(pattern=r"help_back"))
@MK6.on(events.CallbackQuery(pattern=r"help_back"))
@MK7.on(events.CallbackQuery(pattern=r"help_back"))
@MK8.on(events.CallbackQuery(pattern=r"help_back"))
@MK9.on(events.CallbackQuery(pattern=r"help_back"))
@MK10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            MK_Help,
            buttons=[
                [
            Button.inline("● 𝐒ᴘᴀᴍ ●", data="spam"),
            Button.inline("● 𝐑ᴀɪᴅ ●", data="raid"),
           ],
           [
            Button.inline("𝐄xᴛʀᴀ cᴍᴅs", data="extra"),
           ],
           ],
        )           
   else:
        Alert = (
                "Noob !! Make Your Own 🔥 𓆩𝐌𝐀𝐆𝐍𝐄𝐒𝐈𝐔𝐌𓆪 𝗫 𝗦𝗣𝗔𝗠 🔥 Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@MK1.on(events.CallbackQuery(pattern=r"spam"))
@MK2.on(events.CallbackQuery(pattern=r"spam"))
@MK3.on(events.CallbackQuery(pattern=r"spam"))
@MK4.on(events.CallbackQuery(pattern=r"spam"))
@MK5.on(events.CallbackQuery(pattern=r"spam"))
@MK6.on(events.CallbackQuery(pattern=r"spam"))
@MK7.on(events.CallbackQuery(pattern=r"spam"))
@MK8.on(events.CallbackQuery(pattern=r"spam"))
@MK9.on(events.CallbackQuery(pattern=r"spam"))
@MK10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "𝐕𝐚𝐢 !! 𝐊ᴜᴅʜ ᴋᴀ ʙɴᴀ ʟᴇ ɴᴀ ʙsᴅᴋ ʙᴜᴛᴛᴏɴ ᴍᴀɪ ɢàɴᴅ ᴜɴɢʟɪ ɴᴀ ᴋʀ!!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@MK1.on(events.CallbackQuery(pattern=r"raid"))
@MK2.on(events.CallbackQuery(pattern=r"raid"))
@MK3.on(events.CallbackQuery(pattern=r"raid"))
@MK4.on(events.CallbackQuery(pattern=r"raid"))
@MK5.on(events.CallbackQuery(pattern=r"raid"))
@MK6.on(events.CallbackQuery(pattern=r"raid"))
@MK7.on(events.CallbackQuery(pattern=r"raid"))
@MK8.on(events.CallbackQuery(pattern=r"raid"))
@MK9.on(events.CallbackQuery(pattern=r"raid"))
@MK10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "𝑲𝒓 𝒍𝒊𝒚𝒂 𝑺𝒘𝒂𝒈  !! 𝑪𝒉𝒍𝒂 𝒋𝒂 𝒃𝒔𝒅𝒌 𝑲𝒖𝒅𝒉 𝒌𝒂 𝒃𝒏𝒂 𝑩𝒐𝒕 !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@MK1.on(events.CallbackQuery(pattern=r"extra"))
@MK2.on(events.CallbackQuery(pattern=r"extra"))
@MK3.on(events.CallbackQuery(pattern=r"extra"))
@MK4.on(events.CallbackQuery(pattern=r"extra"))
@MK5.on(events.CallbackQuery(pattern=r"extra"))
@MK6.on(events.CallbackQuery(pattern=r"extra"))
@MK7.on(events.CallbackQuery(pattern=r"extra"))
@MK8.on(events.CallbackQuery(pattern=r"extra"))
@MK9.on(events.CallbackQuery(pattern=r"extra"))
@MK10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("◁", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "𝙅𝙪𝙨𝙩 !! 𝙈𝙖𝙠𝙚 𝙮𝙤𝙪𝙧 𝙤𝙬𝙣 𝘽𝙤𝙩𝙨 𝙗𝙧𝙤 𝙩𝙝𝙖𝙩'𝙨 𝙄𝙏 𝙣𝙙 𝙀𝙣𝙟𝙤𝙮 !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
