import asyncio
from pyrogram import Client, filters
from pyrogram.types import (
    Message, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton,
    CallbackQuery
)
from config import API_ID, API_HASH, SESSION_NAME

# Buat client
app = Client(
    session_name=SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH
)

# Handler untuk command /start
@app.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    # Buat inline keyboard dengan button
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ Fitur 1", callback_data="fitur_1"),
                InlineKeyboardButton("🔧 Fitur 2", callback_data="fitur_2")
            ],
            [
                InlineKeyboardButton("📊 Status", callback_data="status"),
                InlineKeyboardButton("ℹ️ Info", callback_data="info")
            ],
            [
                InlineKeyboardButton("🔗 Website", url="https://google.com"),
                InlineKeyboardButton("📞 Kontak", callback_data="kontak")
            ]
        ]
    )
    
    await message.reply_text(
        f"Halo {message.from_user.mention}!\n\n"
        "👋 **Selamat datang di UserBot Saya!**\n\n"
        "Pilih menu di bawah ini:",
        reply_markup=keyboard
    )

# Handler untuk callback dari button
@app.on_callback_query()
async def handle_callback(client: Client, callback_query: CallbackQuery):
    data = callback_query.data
    
    if data == "fitur_1":
        # Keyboard untuk fitur 1
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔙 Kembali", callback_data="back_main")],
                [InlineKeyboardButton("✅ Aktifkan", callback_data="aktif_f1"),
                 InlineKeyboardButton("❌ Matikan", callback_data="nonaktif_f1")]
            ]
        )
        await callback_query.message.edit_text(
            "**✨ Fitur 1**\n\n"
            "Deskripsi: Fitur untuk melakukan X\n"
            "Status: Aktif ✅",
            reply_markup=keyboard
        )
    
    elif data == "fitur_2":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔙 Kembali", callback_data="back_main")],
                [InlineKeyboardButton("⚙️ Settings", callback_data="settings_f2")]
            ]
        )
        await callback_query.message.edit_text(
            "**🔧 Fitur 2**\n\n"
            "Deskripsi: Fitur untuk melakukan Y\n"
            "Status: Nonaktif ❌",
            reply_markup=keyboard
        )
    
    elif data == "status":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔄 Refresh", callback_data="status")],
                [InlineKeyboardButton("🔙 Kembali", callback_data="back_main")]
            ]
        )
        await callback_query.message.edit_text(
            "**📊 Status UserBot**\n\n"
            "• Uptime: 2 jam 30 menit\n"
            "• RAM: 45% digunakan\n"
            "• CPU: 12% digunakan\n"
            "• Pesan diproses: 1245\n",
            reply_markup=keyboard
        )
    
    elif data == "info":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔙 Kembali", callback_data="back_main")]
            ]
        )
        await callback_query.message.edit_text(
            "**ℹ️ Informasi UserBot**\n\n"
            "• Versi: 1.0.0\n"
            "• Dibuat dengan: Pyrogram\n"
            "• Developer: Anda\n"
            "• Update terakhir: 2024",
            reply_markup=keyboard
        )
    
    elif data == "kontak":
        keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("🔙 Kembali", callback_data="back_main")]
            ]
        )
        await callback_query.message.edit_text(
            "**📞 Kontak**\n\n"
            "Telegram: @username\n"
            "Email: email@example.com",
            reply_markup=keyboard
        )
    
    elif data == "back_main":
        # Kembali ke menu utama
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✨ Fitur 1", callback_data="fitur_1"),
                    InlineKeyboardButton("🔧 Fitur 2", callback_data="fitur_2")
                ],
                [
                    InlineKeyboardButton("📊 Status", callback_data="status"),
                    InlineKeyboardButton("ℹ️ Info", callback_data="info")
                ],
                [
                    InlineKeyboardButton("🔗 Website", url="https://google.com"),
                    InlineKeyboardButton("📞 Kontak", callback_data="kontak")
                ]
            ]
        )
        await callback_query.message.edit_text(
            "👋 **Menu Utama**\n\n"
            "Pilih menu di bawah ini:",
            reply_markup=keyboard
        )
    
    elif data == "aktif_f1":
        await callback_query.answer("Fitur 1 diaktifkan!", show_alert=True)
    
    elif data == "nonaktif_f1":
        await callback_query.answer("Fitur 1 dimatikan!", show_alert=True)
    
    elif data == "settings_f2":
        await callback_query.answer("Pengaturan Fitur 2 dibuka!", show_alert=True)
    
    # Hapus loading animation
    await callback_query.answer()

# Command untuk mengirim button di grup
@app.on_message(filters.command("menu") & filters.group)
async def menu_group(client: Client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ Fitur 1", callback_data="fitur_1"),
                InlineKeyboardButton("🔧 Fitur 2", callback_data="fitur_2")
            ],
            [
                InlineKeyboardButton("📊 Status", callback_data="status"),
                InlineKeyboardButton("🔗 Bantuan", url="t.me/username")
            ]
        ]
    )
    
    await message.reply_text(
        "**Menu UserBot**\n\n"
        "Silakan pilih fitur yang tersedia:",
        reply_markup=keyboard
    )

# Command untuk button dengan baris yang berbeda
@app.on_message(filters.command("buttons"))
async def multiple_buttons(client: Client, message: Message):
    # Button dengan 3 baris berbeda
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Button 1", callback_data="btn1")],
            [InlineKeyboardButton("Button 2", callback_data="btn2")],
            [InlineKeyboardButton("Button 3", callback_data="btn3")],
            [InlineKeyboardButton("Button 4", callback_data="btn4")],
            [
                InlineKeyboardButton("Kiri", callback_data="left"),
                InlineKeyboardButton("Tengah", callback_data="center"),
                InlineKeyboardButton("Kanan", callback_data="right")
            ]
        ]
    )
    
    await message.reply_text(
        "Ini contoh button dengan multiple baris:",
        reply_markup=keyboard
    )

# Handler untuk button sederhana
@app.on_callback_query(filters.regex("^btn"))
async def handle_simple_buttons(client: Client, callback_query: CallbackQuery):
    button_num = callback_query.data.replace("btn", "")
    await callback_query.answer(f"Anda menekan Button {button_num}!", show_alert=True)

# Handler untuk arah
@app.on_callback_query(filters.regex("^(left|center|right)$"))
async def handle_direction(client: Client, callback_query: CallbackQuery):
    direction = callback_query.data
    await callback_query.answer(f"Anda memilih: {direction.capitalize()}")

# Command untuk mengirim button dengan URL
@app.on_message(filters.command("links"))
async def send_links(client: Client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🌐 Google", url="https://google.com"),
                InlineKeyboardButton("📚 GitHub", url="https://github.com")
            ],
            [
                InlineKeyboardButton("📺 YouTube", url="https://youtube.com"),
                InlineKeyboardButton("💬 Telegram", url="https://t.me")
            ],
            [InlineKeyboardButton("🔙 Tutup", callback_data="close")]
        ]
    )
    
    await message.reply_text(
        "**Link Cepat**\n\n"
        "Pilih link yang ingin Anda kunjungi:",
        reply_markup=keyboard
    )

# Handler untuk tombol close
@app.on_callback_query(filters.regex("^close$"))
async def close_message(client: Client, callback_query: CallbackQuery):
    await callback_query.message.delete()
    await callback_query.answer("Pesan ditutup!")

# Command untuk contoh button dengan konfirmasi
@app.on_message(filters.command("confirm"))
async def confirm_action(client: Client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✅ Ya", callback_data="confirm_yes"),
                InlineKeyboardButton("❌ Tidak", callback_data="confirm_no")
            ]
        ]
    )
    
    await message.reply_text(
        "Apakah Anda yakin ingin menghapus data ini?",
        reply_markup=keyboard
    )

# Handler untuk konfirmasi
@app.on_callback_query(filters.regex("^confirm_"))
async def handle_confirmation(client: Client, callback_query: CallbackQuery):
    action = callback_query.data
    
    if action == "confirm_yes":
        await callback_query.message.edit_text(
            "✅ Data berhasil dihapus!",
            reply_markup=None
        )
        await callback_query.answer("Data dihapus!")
    else:
        await callback_query.message.edit_text(
            "❌ Penghapusan dibatalkan.",
            reply_markup=None
        )
        await callback_query.answer("Dibatalkan!")

# Command untuk menampilkan button dengan pagination
@app.on_message(filters.command("pages"))
async def show_pages(client: Client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⬅️ Sebelumnya", callback_data="page_1"),
                InlineKeyboardButton("1/3", callback_data="current"),
                InlineKeyboardButton("Selanjutnya ➡️", callback_data="page_2")
            ]
        ]
    )
    
    await message.reply_text(
        "**Halaman 1**\n\n"
        "Ini adalah konten halaman pertama.",
        reply_markup=keyboard
    )

# Run the bot
async def main():
    await app.start()
    print("UserBot berhasil dijalankan!")
    print("Gunakan /start di chat pribadi")
    
    # Keep the bot running
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nUserBot dihentikan.")