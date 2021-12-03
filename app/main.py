from fastapi import FastAPI

from app.db import database, User # This creates all tables on import

app = FastAPI(title="FastAPI, Docker and Traefik!")

#=====================
# Database connection
#=====================
@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy user
    await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


# Get all users
@app.get("/")
async def read_root():
    return await User.objects.all()