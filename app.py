import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import usersRouter
from routes.movie import movie as movie_routes

WEB_URL = os.getenv("WEB_URL")

app = FastAPI(
    title="WatchOne Backend"
)

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    WEB_URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Rutas
app.include_router(usersRouter)
app.include_router(movie_routes)

@app.get("/", tags=["Base"])
def root():
    return {"message": "Ruta principal"}