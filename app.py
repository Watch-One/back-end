from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ruta_inicial():
    return {"message": "Ruta inicial"}