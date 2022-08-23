from bson.objectid import ObjectId
from typing import Union
from decouple import config
import motor.motor_asyncio
from fastapi import Depends, FastAPI, HTTPException, status
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.server.models.user import (
    UserSchema,
    UserResponseSchema
)
MONGO_DETAILS = config("MONGO_DETAILS")
ALGORITHM = "HS256"
JWT_SECRET_KEY = config("JWT_SECRET_KEY")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.MDOMS
user_collection = db.get_collection("user")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

class TokenData(BaseModel):
    username: Union[str, None] = None

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "UserName": user["UserName"],
        "ServiceNumber": user["ServiceNumber"],
        "Email": user["Email"],
        "Password": user["Password"],
        "AffiliatedUnit": user["AffiliatedUnit"],
        "IsOfficer": user["IsOfficer"]
    }

async def check_out_existing_user(ServiceNumber: str) -> bool:
    user = await user_collection.find_one({"ServiceNumber": ServiceNumber})
    if user:
        return True
    else:
        return False

async def retrieve_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users

# Retrieve a student with a matching ID
async def retrieve_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

# Retrieve a student with a matching servicenumber
async def retrieve_user_servicenumber(servicenumber: str) -> dict:
    user = await user_collection.find_one({"ServiceNumber": servicenumber})
    if user:
        return user_helper(user)

async def retrieve_user_servicenumber_nohelper(servicenumber: str) -> dict:
    user = await user_collection.find_one(
        {"ServiceNumber": servicenumber},
        {"_id": 0, "Password": 0}
        )
    if user:
        return user

# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False

# Delete a user from the database
async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True
        
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        servicenumber: str = payload.get("sub")
        if servicenumber is None:
            raise credentials_exception
        token_data = TokenData(username=servicenumber)
    except JWTError:
        raise credentials_exception
    user = await retrieve_user_servicenumber_nohelper(servicenumber)
    if user is None:
        raise credentials_exception 
    print(user)
    return user
 
async def get_current_active_user(current_user: UserResponseSchema = Depends(get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user 
