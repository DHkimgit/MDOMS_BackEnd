from typing import Optional, List
from pydantic import BaseModel, Field

class UnitSchema(BaseModel):
    unit_name: str = Field(...)

    class config():
        schema_extra = {
            "example": {
                "unit_name": "17사단 507여단"
            }
        }
    
