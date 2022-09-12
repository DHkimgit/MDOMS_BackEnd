from bson.objectid import ObjectId
from decouple import config
import motor.motor_asyncio
from typing import List
import json

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.MDOMS
roster_group_collection = db.get_collection("roster_group")

def add_roster_member_group_response_model(data) -> dict:
    return {
        "create_user_id": str(data["create_user_id"]),
        "create_user_name" : data["create_user_name"],
        "roster_group_name": data["roster_group_name"],
        "create_date": data["create_date"],
        "user_edit_permission": data["user_edit_permission"]
    }

async def add_roster_member_group(data: dict) -> dict:
    roster_member_group = await roster_group_collection.insert_one(data)
    result = await 
    print(roster_member_group)
    return add_roster_member_group_response_model(roster_member_group)
