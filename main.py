import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API kalitlari (Render -> Environment Variables'dan olinadi)
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Spotipy mijozini yaratamiz
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎧 Salom! Qaysi musiqani izlaymiz? Faqat nomini yozing.")

# Foydalanuvchi yozgan matndan musiqa qidirish
async def search_music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    results = spotify.search(q=query, limit=1, type='track')

    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        name = track['name']
        artist = track['artists'][0]['name']
        url = track['external_urls']['spotify']
        reply = f"🎵 {name} - {artist}\n🔗 {url}"
    else:
        reply = "😔 Kechirasiz, hech nima topilmadi."

    await update.message.reply_text(reply)

# Asosiy App
if __name__ == '__main__':
    TOKEN = os.getenv("BOT_TOKEN")  # Render serverdagi BOT_TOKEN environment variable

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_music))

    print("Bot ishga tushdi...")
    app.run_polling()
