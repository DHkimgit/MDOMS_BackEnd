from bson.objectid import ObjectId
from decouple import config
import motor.motor_asyncio
from typing import List
import json

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.MDOMS
roster_collection = db.get_collection("roster_information")

def add_roster_information_response_model(data) -> dict:
    return {
        "roster_id" : data["roster_id"],
        "roster_create_user_servicenumber" : data["roster_create_user_servicenumber"],
        "roster_name" : data["roster_name"],
        "roster_work_rule" : data["roster_work_rule"]
    }

async def add_roster_information(data : dict) -> dict:
    roster_data = await roster_collection.insert_one(data)
    inserted_data = await roster_collection.find_one({"roster_id": data["roster_id"]})
    return add_roster_information_response_model(inserted_data)

async def find_roster_information(roster_id: str) -> bool:
    result = roster_collection.find_one({"roster_id": roster_id})
    if result:
        return True
    else:
        return False

async def add_roster_timegroup(roster_id: str, servicenumber: str, appended_data: dict) -> bool:
    roster_information = await roster_collection.find_one({"roster_id": roster_id})
    if roster_information:
        update_timegroup = await roster_collection.update_one(
            {"roster_create_user_servicenumber": servicenumber, "roster_id": roster_id},
            {"$push" : {"roster_time_group" : appended_data}}
        )
        if update_timegroup:
            return True
        return False
