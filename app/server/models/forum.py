from typing import Optional, List
from pydantic import BaseModel, Field

class FourmSchema(BaseModel):
    category: str = Field(...)
    title: str = Field(...)
    content: str = Field(...)

    class config():
        schema_extra = {
            "example": {
                "writer_name": "Jhon doe",
                "writer_service_numer": "22-2222222",
                "category": "general",
                "title": "test",
                "content": "wow",
                "write_date": "2022-09-21",
                "write_time": "12:46:39",
            }
        }

class CommentSchema(BaseModel):
    username: str
    servicenumber: str
    content: str
    comment_date: str

    class config():
        schema_extra = {
            "example": {
                "username": "Jhon doe",
                "servicenumber": "22-2222222",
                "content": "wow",
                "comment_date": "2022-09-21"
            }
        }