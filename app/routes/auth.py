from http import HTTPStatus
import os
from flask import Blueprint, jsonify, request
from flask.cli import load_dotenv

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

load_dotenv()  # Cargar variables de entorno desde el archivo .env

@auth_bp.post('/login')
def get_token():
    auth = request.authorization

    username_auth = os.getenv('USERNAME_AUTH')
    password_auth = os.getenv('PASSWORD_AUTH')

    if not auth or auth.username != username_auth or auth.password != password_auth:
        return {"message": "Faltan credenciales de autenticación."}, HTTPStatus.UNAUTHORIZED    