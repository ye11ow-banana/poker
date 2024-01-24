from decouple import config

DB_HOST = config("POSTGRES_HOST")
DB_PORT = config("POSTGRES_PORT", cast=int)
DB_NAME = config("POSTGRES_DB")
DB_USER = config("POSTGRES_USER")
DB_PASS = config("POSTGRES_PASSWORD")

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = 30
