import os
import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ===============================
# LOAD ENV
# ===============================
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ===============================
# LOGGING
# ===============================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# ===============================
# KEYBOARD
# ===============================
def get_keyboard():
    keyboard = [
        [InlineKeyboardButton("OKE", callback_data="oke")],
        [InlineKeyboardButton("🔄 Refresh", callback_data="retry")]
    ]
    return InlineKeyboardMarkup(keyboard)


# ===============================
# START COMMAND
# ===============================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    name = update.effective_user.first_name or "Teman"

    await update.message.reply_text(
        f"<b>Halo {name}</b> 👋\n\n"
        "Selamat datang di <b>Pemersatu Bangsa</b>\n\n"
        "Untuk mendapatkan <b>500 file</b> yang akan saya bagikan,\n"
        "wajib mengikuti misi dibawah ya.\n\n"
        "Silakan tekan OKE 👇",
        reply_markup=get_keyboard(),
        parse_mode="HTML"
    )


# ===============================
# BUTTON HANDLER
# ===============================
async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    if not query:
        return

    await query.answer()

    if query.data == "oke":
        text = (
            "📌 <b>MISI WAJIB DISELESAIKAN</b>\n\n"
            "🔗 Link pendaftaran:\n"
            "https://d32sk10c4uk0hu.cloudfront.net/bbm/index_1.html?id=85064899\n\n"
            "✅ Login lewat google atau fb\n"
            "✅ Kerjain misinya\n"
            "✅ Wajib rajin login biar dapat reward banyak\n\n"
            "🚀 WAJIB MASUKIN ID REFERRAL = <b>85064899</b>\n\n"
            "Masuk ke game cari menu <b>Invite ID</b> atau <b>ID Referral</b>,\n"
            "masukin <b>85064899</b>.\n\n"
            "Harus benar dimasukin biar terhitung valid\n"
            "dan 500 file bisa diakses."
        )

        await query.edit_message_text(
            text=text,
            reply_markup=get_keyboard(),
            parse_mode="HTML"
        )

    elif query.data == "retry":
        await query.message.reply_text(
            "❌ Kamu belum menyelesaikan misinya!\n\n"
            "🚀 WAJIB MASUKIN ID REFERRAL = 85064899\n\n"
            "Masuk ke game cari Invite ID / ID Referral\n"
            "dan masukkan 85064899 dengan benar.\n\n"
            "Selesaikan dulu misinya biar 500 file bisa kebuka!",
            reply_markup=get_keyboard()
        )


# ===============================
# MAIN
# ===============================
def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN belum diisi di file .env")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button))

    print("✅ Bot aktif bro 🚀")
    app.run_polling()


if __name__ == "__main__":
    main()
