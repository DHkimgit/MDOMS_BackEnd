from typing import Optional, Union
from pydantic import BaseModel, EmailStr, Field, validator

class UserSchema(BaseModel):
    UserName: str = Field(...)
    ServiceNumber: str = Field(...)
    Email: EmailStr = Field(...)
    Password: str = Field(...)
    AffiliatedUnit: str = Field(...)
    IsOfficer: bool = Field(...)

    class config():
        schema_extra = {
            "example": {
                "UserName": "John Doe",
                "ServiceNumber": "22-76458458",
                "Email": "8dnjfekf@gmail.com",
                "Password": "8dnjfekf!",
                "AffiliatedUnit": "Ministy Of Military",
                "IsOfficer": True,
            }
        }
    # @validator('ServiceNumber')
    # def servicenumber_must_have_hyphen(cls, v):
    #     if '-' not in v:
    #         raise ValueError('servicenumber must contain a hyphen')
    #     return v.title()

class UserPatchSchema(BaseModel):
    UserName: Union[str, None] = None
    ServiceNumber: Union[str, None] = None
    Email: Union[EmailStr, None] = None 
    Password: Union[str, None] = None
    AffiliatedUnit: Union[str, None] = None
    IsOfficer: Union[str, None] = None

    class config():
        schema_extra = {
            "example": {
                "UserName": "John Doe",
                "ServiceNumber": "22-76458458",
                "Email": "8dnjfekf@gmail.com",
                "Password": "8dnjfekf!",
                "AffiliatedUnit": "Ministy Of Military",
                "IsOfficer": True,
            }
        }

class UserResponseSchema(BaseModel):
    UserName: str = Field(...)
    ServiceNumber: str = Field(...)
    Email: EmailStr = Field(...)
    AffiliatedUnit: str = Field(...)
    IsOfficer: bool = Field(...)

    class config():
        schema_extra = {
            "example": {
                "UserName": "John Doe",
                "ServiceNumber": "22-76458458",
                "Email": "8dnjfekf@gmail.com",
                "Password": "8dnjfekf!",
                "AffiliatedUnit": "Ministy Of Military",
                "IsOfficer": True,
            }
        }

class UpdateUserModel(BaseModel):
    UserName: Optional[str]
    ServiceNumber: Optional[str]
    Email: Optional[EmailStr]
    Password: Optional[str]
    AffiliatedUnit: Optional[str]
    IsOfficer: Optional[bool]

    class config():
        schema_extra = {
            "example": {
                "UserName": "John Doe",
                "ServiceNumber": "22-76458458",
                "Email": "8dnjfekf@gmail.com",
                "Password": "8dnjfekf!",
                "AffiliatedUnit": "Ministy Of Military",
                "IsOfficer": True,
            }
        }

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}