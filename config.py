import os
from dotenv import load_dotenv

load_dotenv()  # Bu MUHIM

BOT_TOKEN = os.getenv("BOT_TOKEN")
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

print("BOT_TOKEN:", BOT_TOKEN)  # 👈 Test qilish uchun
