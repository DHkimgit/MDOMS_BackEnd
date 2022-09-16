from bson.objectid import ObjectId
from decouple import config
import motor.motor_asyncio
from typing import List
import json

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.MDOMS
roster_group_collection = db.get_collection("roster_group")
user_collection = db.get_collection("user")
def add_roster_member_group_response_model(data) -> dict:
    return {
        "create_user_id": str(data["create_user_id"]),
        "create_user_name" : data["create_user_name"],
        "roster_group_name": data["roster_group_name"],
        "create_date": data["create_date"],
    }

def return_helper(data) -> dict:
    for i in range(len(data["user_edit_permission"])):
        str_id = str(data["user_edit_permission"][i])
        data["user_edit_permission"][i] = str_id
    return {    
        "_id": str(data["_id"]),
        "create_user_id": str(data["create_user_id"]),
        "create_user_name" : data["create_user_name"],
        "roster_group_name": data["roster_group_name"],
        "create_date": data["create_date"],
        "user_edit_permission": data["user_edit_permission"]
    }

async def get_roster_member_groups():
    groups = []
    t = roster_group_collection.find()
    async for group in roster_group_collection.find():
        for i in range(len(group["user_edit_permission"])):
            t = str(group["user_edit_permission"][i])
            group["user_edit_permission"][i] = t
        groups.append(
            {
                "_id": str(group["_id"]),
                "roster_group_name": group["roster_group_name"],
                "create_user_id": str(group["create_user_id"]),
                "create_user_name": group["create_user_name"],
                "create_date": group["create_date"],
                "user_edit_permission": group["user_edit_permission"]
            }
        )
    return groups

async def get_roster_member_group(id: str):
    roster_member_group = await roster_group_collection.find_one({"_id": ObjectId(id)})
    return return_helper(roster_member_group)

async def add_roster_member_group(data: dict) -> str:
    roster_member_group = await roster_group_collection.insert_one(data)
    if roster_member_group:
        return "succesfully added"
    else:
        return "ERROR ㅠㅠ"

async def add_permission(id: str, append_id: str):
    roster_member_group = await roster_group_collection.find_one({"_id": ObjectId(id)})
    if roster_member_group:
        updata_permission = await roster_group_collection.update_one(
            {"_id": ObjectId(id)},
            {"$push" : {"user_edit_permission" : ObjectId(append_id)}}
        )
        result = await roster_group_collection.find_one({"_id": ObjectId(id)})
        print(result)
        return add_roster_member_group_response_model(result)
    else:
        return "Error ㅠㅠ"

async def add_group_member(id: str, append_service_number: str):
    roster_member_group = await roster_group_collection.find_one({"_id": ObjectId(id)})
    if roster_member_group:
        append_member = await user_collection.find_one({"servicenumber": append_service_number})
        if append_member:
            NameWithRank = append_member['rank'] + " " + append_member['name']
            user_id = append_member['_id']
            update_member = await roster_group_collection.update_one(
                {"_id": ObjectId(id)},
                {"$push" : {"member" : {
                    "user_id": user_id,
                    "service_number": append_service_number,
                    "name" : NameWithRank,
                    "status": "normal"
                    }}}
            )
        else:
            return "No matching Servicenumber detected"


async def append_member_status(ids: str, member_servicenumber: str, status: str):
    status = roster_group_collection.update_one(
        {"_id": ObjectId(ids), "member.service_number": member_servicenumber},
        {"$set": {"member.$.status": status}}
        )
    return "done"

async def get_group_members(id: str):
    result = []
    roster_member_group = await roster_group_collection.find_one({"_id": ObjectId(id)})
    print(roster_member_group)
    if roster_member_group:
        for i in range(len(roster_member_group['member'])):
            if roster_member_group['member'][i]['status'] == 'normal':
                result.append(
                    {
                        "service_number": roster_member_group['member'][i]['service_number'],
                        "name": roster_member_group['member'][i]['name'],
                    }
                )
            else:
                continue
    return result