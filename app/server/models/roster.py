from typing import Optional, List
from pydantic import BaseModel, Field


class RosterMemberSchema(BaseModel):
    sequence: int = Field(...)
    name: str = Field(...)
    rank: str = Field(...)
    AffiliatedUnit: str = Field(...)
    state: str = Field(...)

    class Config():
        orm_mode = True

class RosterSchema(BaseModel):
    RosterId: str = Field(...)
    RosterName: str = Field(...)
    Roster: List[RosterMemberSchema]

    class Config():
        orm_mode = True

class UserWithRosterSchema(BaseModel):
    ServiceNumber: str = Field(...)
    Rosters: List[RosterSchema]
    class Config():
        orm_mode = True

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}