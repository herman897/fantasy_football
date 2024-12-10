# this is the app/alpha_service.py file...

import os

from dotenv import load_dotenv


load_dotenv() # looks in the ".env" file for env vars

x_rapidapi_key = os.getenv("x_rapidapi_key", default="demo")
x_rapidapi_host = os.getenv("x_rapidapi_host", default="demo")