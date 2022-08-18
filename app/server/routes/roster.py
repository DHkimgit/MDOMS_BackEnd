from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database.roster import (
    add_roster,
    add_roster2,
    add_roster3,
    find_roster,
    addRosterMemberByServiceNumber,
    retrieve_roster_member
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

@router.post("/", response_description="data added into the database")
async def add_roster_data(roster: RosterSchema = Body(...)):
    rosters = jsonable_encoder(roster)
    new_roster = await add_roster(rosters)
    return ResponseModel(new_roster, "rosters added successfully.")

@router.put("/{id}/memberlist/{roster_id}", response_description="Add member to roster")
async def add_other_roster_data(id: str, roster_id: str, req: UpdateRosterMemberSchema = Body(...)):
    update_data = jsonable_encoder(req)
    updated_roster = await add_roster3(id, roster_id, update_data)
    if updated_roster:
        return ResponseModel(
            "User with ID: {} name update is successful".format(id),
            "User name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )

@router.put("/{servicenumber}/{roster_id}", response_description="Add member to roster by servicenumber")
async def add_roster_member_by_servicenumber(servicenumber: str, roster_id: str, req: UpdateRosterMemberSchema = Body(...)):
    update_member = jsonable_encoder(req)
    updated_roster = await addRosterMemberByServiceNumber(servicenumber, roster_id, update_member)
    if updated_roster:
        return ResponseModel(
            "User with ID: {} name update is successful".format(id),
            "User name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the user data.",
    )

@router.get("/{servicenumber}/{roster_id}", response_description="get roster members")
async def get_member(servicenumber: str, roster_id: str):
    member = await retrieve_roster_member(servicenumber, roster_id)
    if member:
        return member
    return ErrorResponseModel("An error occurred.", 404, "User doesn't exist.")