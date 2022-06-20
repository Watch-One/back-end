import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError

# Usuario y contraseña
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Ip y puerto del servidor con mysql
DB_IP = os.getenv("DB_IP")
DB_PORT = os.getenv("DB_PORT")

# Base de datos a la que se va a conectar
DB_DATABASE = os.getenv("DB_DATABASE")

# Cadena de conexión
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_IP}:{DB_PORT}/{DB_DATABASE}")

meta = MetaData()

# Conectando a la DB
try:
    connection = engine.connect()
    print("DB connected!")
except SQLAlchemyError:
    print("DB not connected!")