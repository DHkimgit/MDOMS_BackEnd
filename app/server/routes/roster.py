from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database.roster import (
    add_roster,
)

from app.server.models.roster import (
    ErrorResponseModel,
    ResponseModel,
    RosterMemberSchema,
    RosterSchema,
    UserWithRosterSchema
)

router = APIRouter()

@router.post("/", response_description="roster data added into the database")
async def add_roster_data(roster: UserWithRosterSchema = Body(...)):
    rosters = jsonable_encoder(roster)
    new_roster = await add_roster(rosters)
    return ResponseModel(new_roster, "rosters added successfully.")

@router.post("/{ServiceNumber}", response_description="roster data added into the database")
async def add_other_roster_data(roster: RosterSchema = Body(...)):
    rosters = jsonable_encoder(roster)
    new_roster = await 