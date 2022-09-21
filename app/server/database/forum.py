from bson.objectid import ObjectId
from decouple import config
import motor.motor_asyncio
from typing import List
import json

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.MDOMS
forum_collection = db.get_collection("forum")
user_collection = db.get_collection("user")
def post_helper(post: dict) -> dict:
    return {
        "writer_name" : post['writer_name'],
        "writer_service_numer" : post["writer_service_numer"],
        "category" : post["category"],
        "title" : post["title"],
        "content" : post["content"],
        "write_date" : post["write_date"],
        "write_time" : post["write_time"]
    }

async def fine_writer_name(servicenumber: str) -> str:
    result = await user_collection.find_one(
        {"servicenumber" : servicenumber}
    )
    name = result["name"]
    return name

async def append_post(post_body : dict) -> bool:
    result = await forum_collection.insert_one(post_body)
    return True

async def get_post(servicenumber: str, write_date: str, write_time: str, category: str) -> dict:
    result = await forum_collection.find_one(
        {"writer_service_numer" : servicenumber, "write_date" : write_date, "write_time": write_time, "category": category}
    )
    print(result)
    return post_helper(result)
