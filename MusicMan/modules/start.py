# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>┗┓ WOY {message.from_user.first_name}  ┏┛\n

❃ dibuat saat sedang sange : [Hehe](https://t.me/milkywaysboys)
━━━━━━━━━━━━━━━
mo culik gua ke Grup lu? culik gua!
</b>""",

# Edit Yang Perlu Lu ganti 
# Tapi Jangan di Hapus Thanks To nya Yaaa :D

        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "🥵 Cara pake 🥵", url="https://t.me/Lunatic0de/20")
                  ],[
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/SharingUserbot"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/allinone_cn"
                    )
                ]
            ]
        ),
     disable_web_page_preview=False
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ **cari link YouTube?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ iya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ kaga ", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**Klik Tombol dibawah biar tau cara pakenya**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥵 Cara Pake 🥵", url="https://t.me/Lunatic0de/20"
                    )
                ]
            ]
        ),
    )  


@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""✅ Bot **berhasil direstart!**\n\n• **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/SharingUserbot"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/milkywaysboys"
                    )
                ]
            ]
        )
   )
