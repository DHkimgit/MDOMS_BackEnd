from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database.logictest import (
    get_roster_member_to_list
)

from app.server.database.logic import (
    get_time_data,
    get_time_group
)

from app.server.models.roster import (
    ErrorResponseModel,
    ResponseModel,
    RosterMemberSchema,
    RosterSchema,
    UpdateRosterSchema,
    UpdateRosterMemberSchema
)

router = APIRouter()

@router.get("/member/{servicenumber}/{roster_id}", response_description="get roster members")
async def get_member(servicenumber: str, roster_id: str):
    member = await get_roster_member_to_list(servicenumber, roster_id)
    if member:
        return member
    return ErrorResponseModel("An error occurred.", 404, "User doesn't exist.")

@router.get("/{roster_id}/{isWeekend}")
async def get_time_array(roster_id: str, isWeekend: bool):
    time_list = await get_time_data(roster_id, isWeekend)
    group_list = await get_time_group(roster_id, isWeekend)
    return time_list, group_list