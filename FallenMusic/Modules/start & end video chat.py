# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

@app.on_message(filters.video_chat_started)
async def brah(client, message):
       await message.reply("• قــام الادمــــن بــفــتــح الــمــحــادثــه الـصـوتـيـه ✓")
@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
       await message.reply("• قــام الادمــــن بـقـفـل الــمــحــادثــه الـصـوتـيـه ✗")
@app.on_message(filters.video_chat_members_invited)
async def fuckoff(client, message):
           text = f"• قــــام ← {message.from_user.mention}"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"\n• بــدعـــوة ←[{user.first_name}](tg://user?id={user.id})"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass  



# @app.on_message(filters.voice_chat_started)
# async def zohary(client: Client, message: Message): 
      # Startt = "عـندي بـرد مش هغني🥲🎧✨"
      # await message.reply_text(Startt)

# @app.on_message(filters.voice_chat_ended)
# async def zoharyy(client: Client, message: Message): 
      # Enddd = "قفله فدماغك🥲💤🎧"
      # await message.reply_text(Enddd)

# async def send_invite(message):
   # for x in message.voice_chat_members_invited.users:
       # try:
        # link = await app.export_chat_invite_link(message.chat.id)
       # except:
        # link = "البوت ليس ادمن لم استطع انشاء رابط"
       # await app.send_message(x.id, f"قام هذا الشخص {message.from_user.mention} \n بدعوتك الي المحادثة الصوتية \nرابط المجموعة : {link}")
# @app.on_message(filters.voice_chat_members_invited)
# async def fuckoff(client: Client, message: Message):
           # text = f"• قام {message.from_user.mention}\n • بدعوة : "
           # x = 0
           # for user in message.voice_chat_members_invited.users:
               # try:
                # text += f"{user.first_name} "
                # x += 1
               # except Exception:
                # pass
           # try:
             # await message.reply_text(f"{text} .")
             # await send_invite(message)
           # except:
             # pass