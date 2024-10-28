# Integrated python modules
from os import getenv

# Modules need to be installed
from dotenv import load_dotenv

# Get token for telegram bot from .env
load_dotenv()

TOKEN = getenv('TOKEN_TG')
ADMINS_TG = getenv('ADMINS_TG').replace(' ', '').split(',')
GIT_URL = getenv('GIT_URL')
DB_NAME = getenv('DB_NAME')