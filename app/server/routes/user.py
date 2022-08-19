from fastapi import APIRouter, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from app.server.database.user import (
    add_user,
    retrieve_users,
    retrieve_user,
    update_user,
    delete_user,
    check_out_existing_user
)
from app.server.models.user import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UpdateUserModel,
)

from app.server.auth.utils import (
    get_hashed_password,
    verify_password,
)

router = APIRouter()

@router.post("/", response_description="User data added into the database")
async def add_student_data(user: UserSchema = Body(...)):
    users = jsonable_encoder(user)
    check_user = await check_out_existing_user(users["ServiceNumber"])
    if check_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this ServiceNumber already exist"
        )
    users["Password"] = get_hashed_password(users["Password"])
    new_user = await add_user(users)
    return ResponseModel(new_user, "User added successfully.")

@router.get("/", response_description="Users retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")

@router.get("/{id}", response_description="User data retrieved")
async def get_user_data(id):
    user = await retrieve_user(id)
    if user:
        return ResponseModel(user, "User data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "User doesn't exist.")

@router.put("/{id}")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            "User with ID: {} name update is successful".format(id),
            "User name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )

@router.delete("/{id}", response_description="User data deleted from the database")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return ResponseModel(
            "User with ID: {} removed".format(id), "User deleted successfully"
        )
    else:
        return ErrorResponseModel(
        "An error occurred", 404, "User with id {0} doesn't exist".format(id)
        )
