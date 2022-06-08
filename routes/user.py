from fastapi import APIRouter, Body
from config.db import connection
from models.user import userModel
from schemas.user import UserSchema, UserLoginSchema
from cryptography.fernet import Fernet
from auth.jwtHandler import signJWT
from schemas.user import UserLoginResponseSchema
from decouple import config

usersRouter = APIRouter()

# Generando key aleatoria para encriptar las contraseñas
key = bytes(config("SECRET_TOKEN"), 'utf-8')
fernet = Fernet(key)

# Ruta para obtener usuario por id
def getUserByEmail(email: str):
    user = connection.execute(userModel.select().where(userModel.c.email == email)).first()
    return user if user else False

# Ruta para crear usuarios
@usersRouter.post("/user/signup", tags=["Users"])
def signup(user: UserSchema = Body(default=None)):
    # Creo objeto con datos del usuario
    new_user = {"name": user.name,
                "email": user.email,
                # Encriptando la contraseña
                "password": fernet.encrypt(user.password.encode("utf-8")),
                "lang": user.lang}
    # Ingreso al usuario a la DB
    result = connection.execute(userModel.insert().values(new_user))

    # Consulto el usuario ingresado a la DB y lo devuelvo
    return signJWT(result.lastrowid)

@usersRouter.post("/user/login", response_model=UserLoginResponseSchema, tags=["Users"])
def login(user: UserLoginSchema = Body(default=None)):
    user_exists = getUserByEmail(user.email)

    if not user_exists or not bytes(user.password, 'utf-8') == fernet.decrypt(bytes(user_exists.password,'utf-8')):
        return {"message": "¡Usuario o contraseña incorrectas!"}

    result = {"message": "¡Inicio de sesión exitoso!", "token": signJWT(user_exists.email)["access_token"]}
    
    return result