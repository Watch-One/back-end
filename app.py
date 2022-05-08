from fastapi import FastAPI
from routes.user import user as user_routes
from routes.movie import movie as movie_routes

app = FastAPI()

app.include_router(user_routes)
app.include_router(movie_routes)