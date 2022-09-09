from typing import Optional, List
from pydantic import BaseModel, Field

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

class RosterInformationResponseSchema(BaseModel):
    roster_id: str = Field(...)
    roster_create_user_servicenumber: str = Field(...)
    roster_name: str = Field(...)
    roster_work_rule: str = Field(...)

    class Config():
        orm_mode = True

class RosterInformationInputSchema(BaseModel):
    roster_id: str = Field(...)
    roster_name: str = Field(...)
    roster_work_rule: str = Field(...)

    class Config():
        orm_mode = True

class RosterInformationTimeGroupSchema(BaseModel):
    time_group_id: str = Field(...)
    time: List[str] = Field(...)
    order: str = Field(...)
    input_person: int = Field(...)
    apply_group: List[str] = Field(...)

    class Config():
        orm_mode = True
