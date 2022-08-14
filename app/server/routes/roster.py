from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database.roster import (
    add_roster,
    add_roster2,
    add_roster3,
    find_roster
)

from app.server.models.roster import (
    ErrorResponseModel,
    ResponseModel,
    RosterMemberSchema,
    RosterSchema,
    UserWithRosterSchema,
    UpdateRosterSchema,
    UpdateRosterMemberSchema
)

router = APIRouter()

@router.post("/", response_description="roster data added into the database")
async def add_roster_data(roster: UserWithRosterSchema = Body(...)):
    rosters = jsonable_encoder(roster)
    new_roster = await add_roster(rosters)
    return ResponseModel(new_roster, "rosters added successfully.")

@router.put("/{id}", response_description="roster data added into the database")
async def add_other_roster_data(id: str, req: UpdateRosterSchema = Body(...)):
    update_member_data = jsonable_encoder(req)
    updated_roster = await add_roster2(id, update_member_data)
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

@router.get("/{id}/memberlist/{roster_id}", response_description="get member")
async def find_roster_member(id: str, roster_id: str):
    roster = await find_roster(id, roster_id)
    if roster:
        return ResponseModel(roster, "wow")