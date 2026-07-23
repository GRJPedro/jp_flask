from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Creamos la instancia de la base de datos sin vincularla a la app todavía
db = SQLAlchemy()
jwt = JWTManager()  # Creamos la instancia de JWTManager sin vincularla a la app todavía