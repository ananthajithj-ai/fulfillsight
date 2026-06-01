from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
TOTAL_RECORDS = os.getenv("TOTAL_RECORDS")
LOG_LEVEL = os.getenv("LOG_LEVEL")