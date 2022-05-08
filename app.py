from fastapi import FastAPI
from routes.user import user as user_routes

app = FastAPI(
    title="WatchOne Backend"
)

app.include_router(user_routes)