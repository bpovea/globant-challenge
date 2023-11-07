import os

DB_USERNAME = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = os.environ["DB_NAME"]

# Configuración de Flask
DEBUG = True
SECRET_KEY = "a379851b-d00b-4ba5-891d-69592913475f"

# Configuración de SQLAlchemy
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
