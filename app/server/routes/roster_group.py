from datetime import date
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter, Body
from fastapi.encoders import jsonable_encoder
from app.server.models.roster_group import (
    RosterGroupInputSchema,
    RosterGroupResponseSchema
)
from app.server.database.user import (
    get_current_active_user_id,
    retrieve_user_name
)
from app.server.database.roster_group import (
    add_roster_member_group,
    add_permission,
    get_roster_member_groups,
    get_roster_member_group,
    add_group_member,
    append_member_status
)
router = APIRouter()

@router.get('/')
async def get_groups():
    groups = await get_roster_member_groups()
    return groups

@router.get('/{id}')
async def get_groups(id: str):
    groups = await get_roster_member_group(id)
    return groups


@router.post('/')
async def post_roster_member(grop_data: RosterGroupInputSchema = Body(...), create_user_id: str = Depends(get_current_active_user_id)):
    appended_data = jsonable_encoder(grop_data)
    appended_data["create_user_id"] = create_user_id
    appended_data["create_user_name"] = await retrieve_user_name(create_user_id)
    appended_data["create_date"] = str(date.today())
    appended_data["user_edit_permission"] = [create_user_id]
    database_append_response = await add_roster_member_group(appended_data)
    return database_append_response

@router.put('/{appended_id}')
async def put_permission_id(id: str, appended_id: str):
    result = await add_permission(id, appended_id)
    return result

@router.put('/{group_id}/{member_servicenumber}')
async def put_group_member(group_id: str, member_servicenumber: str):
    result = await add_group_member(group_id, member_servicenumber)
    return result

@router.put('/{group_id}/{member_servicenumber}/{status}')
async def put_member_status(group_id: str, member_servicenumber: str, status: str):
    result = await append_member_status(group_id, member_servicenumber, status)
    return result