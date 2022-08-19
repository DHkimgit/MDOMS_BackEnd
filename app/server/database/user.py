from bson.objectid import ObjectId
from decouple import config
import motor.motor_asyncio

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.MDOMS
user_collection = db.get_collection("user")

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "UserName": user["UserName"],
        "ServiceNumber": user["ServiceNumber"],
        "Email": user["Email"],
        "Password": user["Password"],
        "AffiliatedUnit": user["AffiliatedUnit"]
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