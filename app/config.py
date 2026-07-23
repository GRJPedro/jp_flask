from datetime import timedelta
import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
    JWT_EXPIRATION_DELTA = timedelta(hours=1)  # Tiempo de expiración del token en segundos (1 hora)
