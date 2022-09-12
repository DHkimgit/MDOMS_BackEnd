from bson.objectid import ObjectId
from decouple import config
import motor.motor_asyncio
from typing import List
import json

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.MDOMS
unit_collection = db.get_collection("unit")
user_collection = db.get_collection("user")
# 출력
def unit_print_helper(data) -> dict:
    return {
        "_id": str(data["_id"]),
        "unit_name": data["unit_name"]
    }

async def get_all_units():
    units = []
    async for unit in unit_collection.find():
        units.append(unit_print_helper(unit))
    return units

async def debug_test():
    test = []
    for i in range(10):
        test.append(i)
    return test

async def add_unit(unit_data: dict) -> dict:
    unit = await unit_collection.insert_one(unit_data)
    result = await unit_collection.find_one({"_id": unit.inserted_id})
    print(result)
    return unit_print_helper(result)

async def delete_unit(id: str) -> bool:
    unit = await unit_collection.find_one({"_id": ObjectId(id)})
    if unit:
        await unit_collection.delete_one({"_id": ObjectId(id)})
        return True
    else:
        False

async def check_root_permission(servicenumber: str) -> bool:
    result = await user_collection.find_one({"servicenumber": servicenumber})
    if result["isofficer"] == True:
        return True
    else:
        return False
