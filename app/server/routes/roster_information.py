from fastapi import FastAPI, status, HTTPException, Depends, APIRouter, Body
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from fastapi.encoders import jsonable_encoder
from app.server.database.user import (
    get_current_active_user_servicenumber
)
from app.server.database.roster_information import (
    add_roster_information,
    find_roster_information,
    add_roster_timegroup
)
from app.server.models.roster_information import (
    RosterInformationResponseSchema,
    RosterInformationInputSchema,
    RosterInformationTimeGroupSchema,
    ResponseModel
)
router = APIRouter()

@router.post('/rosterinformation')
async def post_new_roster_information(roster_information: RosterInformationInputSchema = Body(...), servicenumber: str = Depends(get_current_active_user_servicenumber)):
    appended_data = jsonable_encoder(roster_information)
    appended_data['roster_create_user_servicenumber'] = servicenumber
    database_append_response = await add_roster_information(appended_data, servicenumber)
    return ResponseModel(database_append_response, f"{servicenumber} append roster information data. ID is {appended_data['roster_id']}")

@router.put('/rosterinformation/{roster_id}/timegroup')
async def post_roster_timegroup(roster_id, timegropup_data: RosterInformationTimeGroupSchema = Body(...), servicenumber: str = Depends(get_current_active_user_servicenumber)):
    find = await find_roster_information(roster_id)
    if find == False:
        return {f"roster_id: {roster_id} doesn't exist"}
    else:
        appended_data = jsonable_encoder(timegropup_data)
        database_append_response = await add_roster_timegroup(roster_id, servicenumber, appended_data)
        if database_append_response == True:
            return {f"timegroup data successfully append to roster_id: {roster_id}"}
        else:
            return {f"We Can't append timegroup data to database"}