import dotenv
import os

# load .env to use as default values
dotenv.load_dotenv('.env')

class apiSettings():
    port = os.getenv("API_PORT")

class DatabaseSettings():
    url = os.getenv("DB_URL")
    port = os.getenv("DB_PORT")
    dbname = os.getenv("DB_DBNAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
