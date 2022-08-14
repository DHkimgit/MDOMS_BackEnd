from bson.objectid import ObjectId
from decouple import config
import motor.motor_asyncio

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.MDOMS
roster_collection = db.get_collection("roster")

# helpers
def roster_helper(roster) -> dict:
    return {
        "id": str(roster["_id"]),
        "ServiceNumber": roster["ServiceNumber"],
        "Rosters": {
            "RosterId": roster["Rosters"]["RosterId"],
            "RosterName": roster["Rosters"]["RosterName"]
        }
    }

async def add_roster(roster_data: dict) -> dict:
    roster = await roster_collection.insert_one(roster_data)
    new_roster = await roster_collection.find_one({"_id": roster.inserted_id})
    return {"done"}

async def add_roster2(id: str, roster_data: dict):
    roster = await roster_collection.find_one({"_id": ObjectId(id)})
    if roster:
        updated_roster = await roster_collection.update_one(
            {"_id": ObjectId(id)}, {"$push" : {"Rosters" : roster_data}}
        )
        if updated_roster:
            return True
        return False

async def add_roster3(id: str, roster_id: str, roster_data: dict):
    roster = await roster_collection.find_one({"_id": ObjectId(id)})
    if roster:
        updated_roster = await roster_collection.update_one(
            {"_id": ObjectId(id), "Rosters": {"$elemMatch": {"RosterId": roster_id}}},
            {"$push" : {"Rosters.$.Roster" : roster_data}}
        )
        if updated_roster:
            return True
        return False

async def find_roster(id: str, roster_id: str) -> dict:
    roster = await roster_collection.find_one(
        {
                "_id": ObjectId(id),
                "Rosters": {"RosterId": roster_id}   
        }
    )
    return roster_helper(roster)