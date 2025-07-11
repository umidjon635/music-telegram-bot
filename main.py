import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API sozlamalari
SPOTIFY_CLIENT_ID = os.getenv("d36d17f7f40d4aa18ecbbb12278f8be3")
SPOTIFY_CLIENT_SECRET = os.getenv("432339d8e9cd4a089f9003c0c82becd7")

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 Qaysi musiqani izlaymiz? Faqat nomini yuboring.")

# Foydalanuvchi xabar yuborganida
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    result = spotify.search(q=query, type='track', limit=1)

    if result['tracks']['items']:
        track = result['tracks']['items'][0]
        name = track['name']
        artist = track['artists'][0]['name']
        url = track['external_urls']['spotify']
        message = f"🎧 {name} - {artist}\n🔗 {url}"
    else:
        message = "❌ Musiqa topilmadi."

    await update.message.reply_text(message)

# Botni ishga tushirish
async def main():
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot ishga tushdi...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
