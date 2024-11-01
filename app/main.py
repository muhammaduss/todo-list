import aiohttp
from fastapi import FastAPI
from .services.auth.router import router_auth
from .services.tasks.router import router_task

session = None


app = FastAPI(title="ToDo list application")


@app.on_event("startup")
async def startup_event():
    global session
    session = aiohttp.ClientSession()


@app.on_event("shutdown")
async def shutdown_event():
    await session.close()


app.include_router(router_auth)
app.include_router(router_task)
