from fastapi import FastAPI

from app.database import create_db_and_tables
from app.routers import (
    auth,
    health,
    plans
)

app = FastAPI(
    title="Saanjh Ki Roti API"
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(
    health.router
)

app.include_router(
    auth.router
)

app.include_router(
    plans.router
)