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
    add_roster_member_group
)
router = APIRouter()

@router.post('/')
async def post_roster_member(grop_data: RosterGroupInputSchema = Body(...), create_user_id: str = Depends(get_current_active_user_id)):
    appended_data = jsonable_encoder(grop_data)
    appended_data["create_user_id"] = create_user_id
    appended_data["create_user_name"] = await retrieve_user_name(create_user_id)
    appended_data["create_date"] = str(date.today())
    appended_data["user_edit_permission"] = [create_user_id]
    database_append_response = await add_roster_member_group(appended_data)
    return database_append_response

