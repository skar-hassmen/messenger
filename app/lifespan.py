from contextlib import asynccontextmanager

from fastapi import FastAPI

from models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Startup fastapi")
    yield
    print("Dispose engine")
    await db_helper.dispose()
