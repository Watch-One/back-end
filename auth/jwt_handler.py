import time
from typing import Dict

import jwt
from decouple import config


JWT_SECRET = config("SECRET_TOKEN")
JWT_ALGORITHM = config("ALGORITHM")

# Arma un diccionario con el token
def token_response(token: str):
    return {
        "access_token": token
    }

# Crea el token
def signJWT(user_id: str) -> Dict[str, str]:
    # Diccionario con los datos que se pasan en el token
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    # Se crea el token con los datos, la clave y el algoritmo
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    
    # Devuelve el token armado
    return token_response(token)

# Desencripta el token, obtiene los datos y verifica que sea valido
def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}