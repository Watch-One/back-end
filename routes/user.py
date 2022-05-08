from fastapi import APIRouter
from config.db import connection
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet

user = APIRouter()

# Generando key aleatoria para encriptar las contraseñas
key = Fernet.generate_key()
f = Fernet(key)


# Ruta para obtener usuario por id
@user.get("/user/{id}")
def get_user(id: str):
    __user = connection.execute(users.select().where(users.c.id == id)).first()

    user = {
        "name": __user["name"],
        "email": __user["email"]
    }
    return user


# Ruta para crear usuarios
@user.post("/user/create")
def create_user(user: User):
    # Creo objeto con datos del usuario
    new_user = {"name": user.name,
                "email": user.email,
                # Encriptando la contraseña
                "password": f.encrypt(user.password.encode("utf-8"))}

    # Ingreso al usuario a la DB
    result = connection.execute(users.insert().values(new_user))

    # Consulto el usuario ingresado a la DB y lo devuelvo
    return connection.execute(users.select().where(users.c.id == result.lastrowid)).first()
