from typing import Optional, Union
from pydantic import BaseModel, EmailStr, Field, validator

class UserSchema(BaseModel):
    name: str = Field(...)
    rank: str = Field(...)
    servicenumber: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    unit: str = Field(...)
    isofficer: bool = Field(...)

    class config():
        schema_extra = {
            "example": {
                "name": "John Doe",
                "rank": "일병",
                "servicenumber": "22-76458458",
                "email": "8dnjfekf@gmail.com",
                "password": "8dnjfekf!",
                "unit": "Ministy Of Military",
                "isofficer": True,
            }
        }
    # @validator('ServiceNumber')
    # def servicenumber_must_have_hyphen(cls, v):
    #     if '-' not in v:
    #         raise ValueError('servicenumber must contain a hyphen')
    #     return v.title()

class UserPatchSchema(BaseModel):
    name: Union[str, None] = None
    rank: Union[str, None] = None
    servicenumber: Union[str, None] = None
    email: Union[EmailStr, None] = None 
    password: Union[str, None] = None
    unit: Union[str, None] = None
    isofficer: Union[str, None] = None

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
    name: str = Field(...)
    rank: str = Field(...)
    servicenumber: str = Field(...)
    email: EmailStr = Field(...)
    unit: str = Field(...)
    isofficer: bool = Field(...)

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
    name: Optional[str]
    rank: Optional[str]
    servicenumber: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    unit: Optional[str]
    isofficer: Optional[bool]

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