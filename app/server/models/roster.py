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

class UpdateRosterSchema(BaseModel):
    RosterId: Optional[str]
    RosterName: Optional[str]
    class Config():
        schema_extra = {
            "example": {
                "RosterId": "01",
                "RosterName": "무전실 근무",
            }
        }

class UpdateRosterMemberSchema(BaseModel):
    sequence: Optional[int]
    name: Optional[str]
    rank: Optional[str]
    AffiliatedUnit: Optional[str]
    state: Optional[str]

    class Config():
        schema_extra = {
            "example": {
                "sequence": "2",
                "name": "이정현",
                "rank": "상병",
                "AffiliatedUnit": "통신중대",
                "state": "영내",
            }
        }

class RosterSchema(BaseModel):
    ServiceNumber: str = Field(...)
    RosterId: str = Field(...)
    RosterName: str = Field(...)

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