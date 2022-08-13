from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    UserName: str = Field(...)
    ServiceNumber: str = Field(...)
    Email: EmailStr = Field(...)
    Password: str = Field(...)
    AffiliatedUnit: str = Field(...)

    class config():
        schema_extra = {
            "example": {
                "UserName": "John Doe",
                "ServiceNumber": "22-76458458",
                "Email": "8dnjfekf@gmail.com",
                "Password": "8dnjfekf!",
                "AffiliatedUnit": "Ministy Of Military",
            }
        }

class UpdateUserModel(BaseModel):
    UserName: Optional[str]
    ServiceNumber: Optional[str]
    Email: Optional[EmailStr]
    Password: Optional[str]
    AffiliatedUnit: Optional[str]

    class config():
        schema_extra = {
            "example": {
                "UserName": "John Doe",
                "ServiceNumber": "22-76458458",
                "Email": "8dnjfekf@gmail.com",
                "Password": "8dnjfekf!",
                "AffiliatedUnit": "Ministy Of Military",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}