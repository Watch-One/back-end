from fastapi import APIRouter, Body
from config.db import connection
from models.user import userModel
from schemas.user import UserSchema, UserLoginSchema
from cryptography.fernet import Fernet
from auth.jwt_handler import signJWT
from schemas.response import LoginResponseSchema

usersRouter = APIRouter()

# Generando key aleatoria para encriptar las contraseñas
key = Fernet.generate_key()
f = Fernet(key)


# Ruta para obtener usuario por id
#@usersRouter.get("/user/{id}", response_model=UserSchema, tags=["Users"])
def getUserByEmail(email: str):
    # TODO: Controlar error cuando no existe ususario con ese id
    return connection.execute(userModel.select().where(userModel.c.email == email)).first()

# Ruta para crear usuarios
@usersRouter.post("/user/signup", tags=["Users"])
def signup(user: UserSchema = Body(default=None)):
    # Creo objeto con datos del usuario
    new_user = {"name": user.name,
                "email": user.email,
                # Encriptando la contraseña
                "password": f.encrypt(user.password.encode("utf-8")),
                "lang": user.lang}

    # Ingreso al usuario a la DB
    result = connection.execute(userModel.insert().values(new_user))

    # Consulto el usuario ingresado a la DB y lo devuelvo
    return signJWT(result.lastrowid)

@usersRouter.post("/user/login", response_model=LoginResponseSchema , tags=["Users"])
def login(user: UserLoginSchema = Body(default=None)):
    user_exists = connection.execute(userModel.select().where(userModel.c.email == user.email)).first()

    if not user_exists:
        result = {"message": "Usuario o contraseña incorrectas."}
        return result


    result = {"message": "Inicio de sesión exitoso.", "token": signJWT(user_exists.id)["access_token"]}
    
    return result