import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# UPS API Credentials (Stored in .env)
UPS_CLIENT_ID = os.getenv("UPS_CLIENT_ID")
UPS_CLIENT_SECRET = os.getenv("UPS_CLIENT_SECRET")

# Base Directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File Paths
DATA_PATH = os.path.join(BASE_DIR, "../data/UPS_Facilities.csv")
