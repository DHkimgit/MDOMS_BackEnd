from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
# from app.schemas import UserOut, UserAuth, TokenSchema
from app.server.models.user import (
    TokenSchema,
    UserSchema,
    UserResponseSchema
)
from app.server.auth.utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)

from app.server.database.user import (
    check_out_existing_user,
    retrieve_user_servicenumber,
    get_current_active_user,
    get_current_user
)

router = APIRouter()
# https://www.freecodecamp.org/news/how-to-add-jwt-authentication-in-fastapi/
@router.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    usercheck = await check_out_existing_user(form_data.username)
    if usercheck is False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    user = await retrieve_user_servicenumber(form_data.username)
    hashed_pass = user['password']

    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    return {
        "access_token": create_access_token(user['servicenumber']),
        "refresh_token": create_refresh_token(user['servicenumber']),
    }

@router.get("/users/me/")
async def read_users_me(current_user: UserSchema = Depends(get_current_active_user)):
    return current_user

@router.get("/me/{token}")
async def get_user(token: str):
    user = await get_current_user(token)
    return user