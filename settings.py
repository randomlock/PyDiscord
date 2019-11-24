import os

from dotenv import load_dotenv

load_dotenv()

# CREDENTIALS
TOKEN = os.getenv('DISCORD_TOKEN')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
GOOGLE_API_KEY = os.getenv('GOOGLE_SEARCH_API_KEY')
GOOGLE_CSE_KEY = os.getenv('GOOGLE_CSE_ID')

# ERROR MESSAGE
INPUT_REQUIRED_ERROR_MSG = 'Please enter required input'
GOOGLE_NO_RESULT_MSG = 'No result found. Please try some other search'
MAX_LENGTH_ERROR_MSG = 'Input should be less than 255 characters'

# EMBED CONFIG
EMBED_COLOR = 0x00ff40

# INPUT CONSTRAINT
INPUT_MAX_LENGTH = 255

# CLIENT MESSAGE
CLIENT_INPUT_GREETING = 'hi'
CLIENT_OUTPUT_GREETING = 'Hey'

# OTHER_ CONFIG
MAX_SEARCH_HISTORY_RESULT_COUNT = 5
MAX_SEARCH_RESULT_COUNT = 5
