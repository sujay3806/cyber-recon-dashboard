# config.py
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")


VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NVD_API_KEY = os.getenv("NVD_API_KEY")

SCAN_TIMEOUT=1
MAX_CONCURRENT_CONNECTIONS=500

