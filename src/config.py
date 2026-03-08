import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("API_KEY")
PLAYLIST_ID = os.getenv("PLAYLIST_ID")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")

CREDENTIALS_FILE = "credentials.json"