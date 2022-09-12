from typing import Optional, List
from pydantic import BaseModel, Field

# 초기 그룹 생성 api 요청시 스키마
class RosterGroupInputSchema(BaseModel):
    roster_group_name: str = Field(...)
    class Config():
        orm_mode = True

class RosterGroupResponseSchema(BaseModel):
    create_user_id: str = Field(...)
    create_user_name: str = Field(...)
    roster_group_name: str = Field(...)
    create_date: str = Field(...)
    user_edit_permission: List[str] = Field(...)
    member: List[dict]
    class Config():
        orm_mode = True