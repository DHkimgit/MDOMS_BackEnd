from bson.objectid import ObjectId
from decouple import config
import motor.motor_asyncio
from typing import List
import json

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.MDOMS
roster_collection = db.get_collection("roster_information")

# 시간 데이터를 배열로 리턴합니다.
async def get_time_data(roster_id: str, isWeekend:bool):
    result = []
    if isWeekend:
        data = await roster_collection.find_one({"_id": ObjectId(roster_id)})
        for i in range(len(data['roster_time_group'])):
            if 'weekend' in data['roster_time_group'][i]['apply_group']:
                for j in range(len(data['roster_time_group'][i]['time'])):
                    result.append(data['roster_time_group'][i]['time'][j])
        return result
    else:
        data = await roster_collection.find_one({"_id": ObjectId(roster_id)})
        for i in range(len(data['roster_time_group'])):
            if 'weekday' in data['roster_time_group'][i]['apply_group']:
                for j in range(len(data['roster_time_group'][i]['time'])):
                    result.append(data['roster_time_group'][i]['time'][j])
        return result

async def get_time_group(roster_id: str, isWeekend:bool):
    time_group = []
    result = []
    if isWeekend:
        data = await roster_collection.find_one({"_id": ObjectId(roster_id)})
        for i in range(len(data['roster_time_group'])):
            if 'weekend' in data['roster_time_group'][i]['apply_group']:
                time_group.append(data['roster_time_group'][i]['time'])
        time_group.sort()
        for j in range(len(time_group)):
            result.append(len(time_group[j]))
        return result
    else:
        data = await roster_collection.find_one({"_id": ObjectId(roster_id)})
        for i in range(len(data['roster_time_group'])):
            if 'weekday' in data['roster_time_group'][i]['apply_group']:
                time_group.append(data['roster_time_group'][i]['time'])
        time_group.sort()
        for j in range(len(time_group)):
            result.append(len(time_group[j]))
        return result