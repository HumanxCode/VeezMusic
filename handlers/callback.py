# (C) 2021 VeezMusic-Project

from helpers.decorators import authorized_users_only
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) memungkinkan Anda memutar musik di grup melalui obrolan suara Telegram baru!**

💡 **Cari tahu semua perintah Bot dan cara kerjanya dengan mengklik » 📚 Tombol perintah!**

🔖 **Untuk mengetahui cara menggunakan bot ini, silakan klik tombol » ❓ Tombol Panduan Dasar**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Tambahkan saya ke Grup Anda ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Panduan Dasar", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Perintah", Panduan Dasarcallback_data="cbcmds"),
                    InlineKeyboardButton("❤️ Donasi", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Halo !**

» **tekan tombol di bawah untuk membaca penjelasan dan melihat daftar perintah yang tersedia !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 Basic Cmd", callback_data="cbbasic"),
                    InlineKeyboardButton("📕 Advanced Cmd", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("📘 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("📗 Sudo Cmd", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("📙 Owner Cmd", callback_data="cbowner")],
                [InlineKeyboardButton("🔙 Kembali", callback_data="cbguide")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **di sini adalah perintah dasar**

🎧 [ VOICE CHAT PLAY CMD ]

/play (judul lagu) - putar lagu dari youtube
/ytp (judul lagu) - putar lagu langsung dari youtube
/stream (reply to audio) - putar lagu menggunakan file audio
/playlist - tampilkan daftar lagu dalam antrian
/song (judul lagu) - download lagu dari youtube
/search (nama video) - cari video dari youtube detail
/video (nama video) - unduh video dari youtube terperinci
/lyric - (judul lagu) penghapus lirik

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **di sini adalah perintah lanjutan**

/start (in group) - lihat status bot hidup
/reload - muat ulang bot dan segarkan daftar admin
/ping - periksa status ping bot
/uptime - periksa status waktu aktif bot
/id - tunjukkan grup/id pengguna & lainnya

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **ini perintah adminnya**

/player - tampilkan status pemutaran musik
/pause - jeda streaming musik
/resume - lanjutkan musik yang dijeda
/skip - lompat ke lagu berikutnya
/end - hentikan streaming musik
/join - undang userbot bergabung ke grup Anda
/leave - perintahkan bot pengguna untuk keluar dari grup Anda
/auth - authorized user for using music bot
/unauth - unauthorized for using music bot
/control - buka panel pengaturan pemutar
/delcmd (on | off) - enable / disable del cmd feature
/music (on / off) - disable / enable music player in your group

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the sudo commands**

/leaveall - perintahkan asisten untuk pergi dari semua grup
/stats - tunjukkan statistik bot
/rmd - hapus semua file yang diunduh
/clear - hapus semua file .jpg
/eval (query) - mengeksekusi kode
/sh (query) - menjalankan kode

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **ini perintah owner**

/stats - tunjukkan statistik bot
/broadcast (reply to message) - kirim pesan siaran dari bot
/block (user id - duration - reason) - blokir pengguna karena menggunakan bot Anda
/unblock (user id - reason) - buka blokir pengguna yang Anda blokir karena menggunakan bot Anda
/blocklist - menunjukkan kepada Anda daftar pengguna yang diblokir karena menggunakan bot Anda

📝 note: semua perintah yang dimiliki oleh bot ini dapat dijalankan oleh pemilik bot tersebut tanpa ada pengecualian.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbhelp")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **CARA MENGGUNAKAN BOT INI:**

1.) **pertama, tambahkan saya ke grup Anda.**
2.) **kemudian promosikan saya sebagai admin dan berikan semua izin kecuali admin anonim.**
3.) **setelah mempromosikan saya, ketik /reload di grup untuk memperbarui daftar admin.**
3.) **tambahkan @{ASSISTANT_NAME} ke grup Anda atau ketik /join untuk mengundangnya.**
4.) **nyalakan obrolan video terlebih dahulu sebelum mulai memutar musik.**

📌 **jika userbot belum join ke video chat pastikan video chat sudah aktif, atau ketik /leave lalu ketik /join lagi.**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📚 Command List", callback_data="cbhelp")],
                [InlineKeyboardButton("🗑 Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
async def cbback(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 hanya admin yang dapat menekan tombol ini !", show_alert=True)
    await query.edit_message_text(
        "**💡 di sini adalah menu kontrol bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⏸ pause", callback_data="cbpause"),
                    InlineKeyboardButton("▶️ resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("⏩ skip", callback_data="cbskip"),
                    InlineKeyboardButton("⏹ stop", callback_data="cbend"),
                ],
                [InlineKeyboardButton("⛔ anti cmd", callback_data="cbdelcmds")],
                [InlineKeyboardButton("🗑 Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
async def cbdelcmds(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 hanya admin yang dapat menekan tombol ini !", show_alert=True)
    await query.edit_message_text(
        f"""📚 **ini adalah informasi fitur:**
        
**💡 Feature:** hapus setiap perintah yang dikirim oleh pengguna untuk menghindari spam di grup !

❔ usage:**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

» **tekan tombol di bawah untuk membaca penjelasan dan melihat daftar perintah yang tersedia !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📚 Basic Cmd", callback_data="cblocal"),
                    InlineKeyboardButton("📕 Advanced Cmd", callback_data="cbadven"),
                ],
                [
                    InlineKeyboardButton("📘 Admin Cmd", callback_data="cblamp"),
                    InlineKeyboardButton("📗 Sudo Cmd", callback_data="cblab"),
                ],
                [InlineKeyboardButton("📙 Owner Cmd", callback_data="cbmoon")],
                [InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **CARA MENGGUNAKAN BOT INI:**

1.) **pertama, tambahkan saya ke grup Anda.**
2.) **kemudian promosikan saya sebagai admin dan berikan semua izin kecuali admin anonim.**
3.) **setelah mempromosikan saya, ketik /reload dalam grup untuk memperbarui daftar admin.**
3.) **tambahkan @{ASSISTANT_NAME} ke grup Anda atau ketik /join untuk mengundangnya.**
4.) **nyalakan obrolan video terlebih dahulu sebelum mulai memutar musik.**

📌 **jika userbot belum join ke video chat pastikan video chat sudah aktif, atau ketik /leave lalu ketik /join lagi.**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblocal"))
async def cblocal(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the basic commands**

🎧 [ VOICE CHAT PLAY CMD ]

/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/video (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadven"))
async def cbadven(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **di sini adalah perintah lanjutan**

/start (in group) - lihat status bot hidup
/reload - muat ulang bot dan segarkan daftar admin
/ping - periksa status ping bot
/uptime - periksa status waktu aktif bot
/id - tunjukkan grup/id pengguna & lainnya

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblamp"))
async def cblamp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the admin commands**

/player - tampilkan status pemutaran musik
/pause - jeda streaming musik
/resume - lanjutkan musik yang dijeda
/skip - lompat ke lagu berikutnya
/end - hentikan streaming musik
/join - undang userbot bergabung ke grup Anda
/leave - perintahkan bot pengguna untuk keluar dari grup Anda
/auth - pengguna resmi untuk menggunakan bot musik
/unauth - unauthorized for using music bot
/control - buka panel pengaturan pemutar
/delcmd (on | off) - enable / disable fitur del cmd
/music (on / off) - disable / enable pemutar musik di grup Anda

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cblab"))
async def cblab(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **di sini adalah perintah sudo**

/leaveall - perintahkan asisten untuk pergi dari semua grup
/stats - tunjukkan statistik bot
/rmd - hapus semua file yang diunduh
/clear - hapus semua file .jpg
/eval (query) - mengeksekusi kode
/sh (query) - menjalankan kode

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmoon"))
async def cbmoon(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **here is the owner commands**

/stats - tunjukkan statistik bot
/broadcast - kirim pesan siaran dari bot
/block (user id - duration - reason) - blokir pengguna karena menggunakan bot Anda
/unblock (user id - reason) - buka blokir pengguna yang Anda blokir karena menggunakan bot Anda
/blocklist - menunjukkan kepada Anda daftar pengguna yang diblokir karena menggunakan bot Anda

📝 note: semua perintah yang dimiliki oleh bot ini dapat dijalankan oleh pemilik bot tersebut tanpa ada pengecualian.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cmdhome"))
async def cmdhome(_, query: CallbackQuery):
    
    bttn = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Aturan Perintah", callback_data="cmdsyntax")
            ],[
                InlineKeyboardButton("🗑 Close", callback_data="close")
            ]
        ]
    )
    
    nofound = "😕 **tidak dapat menemukan lagu yang Anda minta**\n\n» **tolong berikan nama lagu yang benar atau sertakan nama artis juga**"
    
    await query.edit_message_text(nofound, reply_markup=bttn)


@Client.on_callback_query(filters.regex("cmdsyntax"))
async def cmdsyntax(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Aturan Perintah** untuk memutar musik di **Obrolan Suara:**
• `/play (query)` - untuk memutar musik melalui youtube
• `/ytp (query)` - untuk memutar musik langsung melalui youtube

⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cmdhome")]]
        ),
    )
