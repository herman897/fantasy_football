# this is the app/tank01_service.py file...

import os

from dotenv import load_dotenv

BASE_URL = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
load_dotenv() # looks in the ".env" file for env vars

HEADERS = {
    "X-RapidAPI-Key": os.getenv("x_rapidapi_key", default="demo"),
    "X-RapidAPI-Host": os.getenv("x_rapidapi_host", default="demo")
}