from bson.objectid import ObjectId
from decouple import config
import motor.motor_asyncio

MONGO_DETAILS = config("MONGO_DETAILS")
# db = client['MDOMS']
# user = db['Users']
# client = MongoClient(MONGO_DETAILS)

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.MDOMS
roster_collection = db.get_collection("roster")
# helpers

def roster_helper(roster) -> dict:
    return {
        "id": str(roster["_id"]),
        "UserName": roster["UserName"],
        "ServiceNumber": roster["ServiceNumber"],
        "Email": roster["Email"],
        "Password": roster["Password"],
        "AffiliatedUnit": roster["AffiliatedUnit"]
    }

async def add_roster(roster_data: dict) -> dict:
    roster = await roster_collection.insert_one(roster_data)
    new_roster = await roster_collection.find_one({"_id": roster.inserted_id})
    return {"done"}

async def add_roster2(roster_data: dict, ServiceNumber: dict) -> dict:
    roster = await roster_collection.find_one({"ServiceNumber": ServiceNumber})
    
    roster = await roster_collection.insert_one(roster_data)
    new_roster = await roster_collection.find_one({"_id": roster.inserted_id})
    return {"done"}