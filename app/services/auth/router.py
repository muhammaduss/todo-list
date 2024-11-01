from fastapi import APIRouter

from app.services.auth.service import Authentication

router_auth = APIRouter(prefix="/auth", tags=["Authentification"])


@router_auth.get("/")
def hi():
    return "hi"


@router_auth.post("/register", summary="register user")
async def register():
    return await Authentication.register()


@router_auth.post("/login", summary="login user")
async def login():
    return await Authentication.login()


@router_auth.post("/refresh", summary="refresh token")
async def refresh():
    return await Authentication.refresh()
