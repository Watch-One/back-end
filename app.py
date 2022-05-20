from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import user as user_routes
from routes.movie import movie as movie_routes

app = FastAPI(
    title="WatchOne Backend"
)

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes)
app.include_router(movie_routes)