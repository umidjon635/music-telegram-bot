import logging
from yt_dlp import YoutubeDL
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Logger sozlash
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Qaysi qo‘shiqni izlaymiz? 🎵")

# Musiqa qidirish va yuborish
async def search_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    await update.message.reply_text("🔍 Qidirilmoqda...")

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
            url = info['webpage_url']
            title = info['title']
            await update.message.reply_text(f"Topildi: {title}\nYuklanmoqda...")

            ydl.download([url])
            file_name = ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3")

            await update.message.reply_audio(audio=open(file_name, 'rb'), title=title)
        except Exception as e:
            await update.message.reply_text(f"Xatolik yuz berdi: {str(e)}")

# Botni ishga tushirish
def main():
    from config import BOT_TOKEN

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_music))

    app.run_polling()

if __name__ == '__main__':
    main()
