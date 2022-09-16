from bson.objectid import ObjectId
from decouple import config
from datetime import datetime, date
import motor.motor_asyncio
from typing import List
import json

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.MDOMS

roster_group_collection = db.get_collection("roster_group")
user_collection = db.get_collection("user")
roster_collection = db.get_collection("roster_information")
schedule_collection = db.get_collection("schedule")

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


class date_parser:
    def year(date):
        return date[0]+date[1]+date[2]+date[3]

    def month(date):
        return date[5]+date[6]

    def date(date):
        return date[8]+date[9]

    def is_weekend(date):
        today = datetime(int(date_parser.year(date)), int(date_parser.month(date)), int(date_parser.date(date))).weekday()
        if today==5 or today == 6:
            return True
        else:
            return False

    def day(date):
        today = datetime(int(date_parser.year(date)), int(date_parser.month(date)), int(date_parser.date(date))).weekday()
        if today == 0:
            return "월요일"
        elif today == 1:
            return "화요일"
        elif today == 2:
            return "수요일"
        elif today == 3:
            return "목요일"
        elif today == 4:
            return "금요일"
        elif today == 5:
            return "토요일"
        else:
            return "일요일"

# date = '2022-09-15'
async def make_daily_schedule(user_id: str, roster_id: str, roster_group_id: str, date: str, prev_date: str):
    schedule = []
    membergroup = []
    time_data = []
    time_group_data = []
    time_group = []
    pointer = 0
    day = date_parser.day(date)
    isWeekend = date_parser.is_weekend(date)
    roster_information = await roster_collection.find_one({"_id": ObjectId(roster_id)})
    roster_name = roster_information['roster_name']
    prev_schedule_data = await schedule_collection.find_one(
        {"date" : prev_date, "create_user_id" : user_id, "roster_information_id" : roster_id}
    )
    print(prev_schedule_data)
    append_schedule_document = await schedule_collection.insert_one({
        "create_user_id": user_id,
        "roster_information_id": roster_id,
        "roster_name": roster_name,
        "date": date,
        "isweekend": isWeekend
    })
    roster_member_group = await roster_group_collection.find_one({"_id": ObjectId(roster_group_id)})
    if roster_member_group:
        for i in range(len(roster_member_group['member'])):
            if roster_member_group['member'][i]['status'] == 'normal':
                membergroup.append(
                    {
                        "service_number": roster_member_group['member'][i]['service_number'],
                        "name": roster_member_group['member'][i]['name'],
                    }
                )   
            else:
                continue

    update_document = await schedule_collection.update_one(
        {"roster_information_id": roster_id, "date": date},
        {"$set": {"member" : membergroup}}
        )

    if isWeekend:
        data = await roster_collection.find_one({"_id": ObjectId(roster_id)})
        for i in range(len(data['roster_time_group'])):
            if 'weekend' in data['roster_time_group'][i]['apply_group']:
                for j in range(len(data['roster_time_group'][i]['time'])):
                    time_data.append(data['roster_time_group'][i]['time'][j])

    else:
        data = await roster_collection.find_one({"_id": ObjectId(roster_id)})
        for i in range(len(data['roster_time_group'])):
            if 'weekday' in data['roster_time_group'][i]['apply_group']:
                for j in range(len(data['roster_time_group'][i]['time'])):
                    time_data.append(data['roster_time_group'][i]['time'][j])

    if isWeekend:
        data = await roster_collection.find_one({"_id": ObjectId(roster_id)})
        for i in range(len(data['roster_time_group'])):
            if 'weekend' in data['roster_time_group'][i]['apply_group']:
                time_group.append(data['roster_time_group'][i]['time'])
        time_group.sort()
        for j in range(len(time_group)):
            time_group_data.append(len(time_group[j]))

    else:
        data = await roster_collection.find_one({"_id": ObjectId(roster_id)})
        for i in range(len(data['roster_time_group'])):
            if 'weekday' in data['roster_time_group'][i]['apply_group']:
                time_group.append(data['roster_time_group'][i]['time'])
        time_group.sort()
        for j in range(len(time_group)):
            time_group_data.append(len(time_group[j]))
    
    time_pointer = 0

    
    
    list(prev_schedule_data['next_pointer'][i].values())[0]
    for i in range(len(prev_schedule_data['next_pointer'])):
        for j in range(len(membergroup)):
            if membergroup[j]['name'] == list(prev_schedule_data['next_pointer'][i].values())[0]:
                time_group_data_pointer.append(j)
    if prev_schedule_data:
        pointer = 1
    else:
        pointer = 0
    
    # [1, 5]
    for i in range(len(time_group_data)):
        j = time_group_data[i]
        user_pointer = 0
        member_pointer = time_group_data_pointer[i]
        for k in range(j):
            if pointer == 0:
                update_document = await schedule_collection.update_one(
                    {"roster_information_id": roster_id, "date": date},
                    {"$push": {"schedule" : {f"{time_data[k + time_pointer]}": f"{membergroup[k].values()}"}}}
                )
            else:
                update_document = await schedule_collection.update_one(
                    {"roster_information_id": roster_id, "date": date},
                    {"$push": {"schedule" : {f"{time_data[k + time_pointer]}": f"{membergroup[k + member_pointer]['name']}"}}}
                )
            user_pointer += 1
        
        pointer_time = time_data[i][0] + time_data[i][1] + ':' +  time_data[i][3] + time_data[i][4] + ' ' + '-' + ' ' + time_data[i + j - 1][8] + time_data[i + j - 1][9] + ':' + time_data[i + j - 1][11] + time_data[i + j - 1][12]
        if pointer==0:
            update_document = await schedule_collection.update_one(
                        {"roster_information_id": roster_id, "date": date},
                        {"$push": {"next_pointer" : {f"{pointer_time}": f"{membergroup[user_pointer]['name']}"}}}
                    )
        else:
            update_document = await schedule_collection.update_one(
                        {"roster_information_id": roster_id, "date": date},
                        {"$push": {"next_pointer" : {f"{pointer_time}": f"{membergroup[user_pointer + member_pointer]['name']}"}}}
                    )
        

        time_pointer += time_group_data[i]


    return "ok"
# membergroup
# time_data
#   [
#     "06:00 - 08:00",
#     "08:00 - 10:00",
#     "10:00 - 12:00",
#     "12:00 - 14:00",
#     "14:00 - 16:00",
#     "18:00 - 18:00"
#   ],
#   [
#     1,
#     5
#   ]
    
