from bson.objectid import ObjectId
from decouple import config
import motor.motor_asyncio
from typing import List
import json

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.MDOMS
roster_collection = db.get_collection("roster")

async def get_roster_member_to_list(servicenumber: str, roster_id: str) -> List:
    member = await roster_collection.find_one(
        {"ServiceNumber": servicenumber, "RosterId": roster_id},
        {"_id": False, "ServiceNumber": False, "RosterId": False, "RosterName": False}
    )
    my_json_str = json.dumps(member)
    jsonData = json.loads(my_json_str)
    member_list = jsonData['RosterMember']
    result = []
    for i in range(len(member_list)):
        sequence = member_list[i]['sequence']
        rank = member_list[i]['rank']
        name = member_list[i]['name']
        result.append(f'{rank} {name}')
    print(result)
    
    if member:
        return result
