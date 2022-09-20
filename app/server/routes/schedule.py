from fastapi import FastAPI, status, HTTPException, Depends, APIRouter, Body
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from fastapi.encoders import jsonable_encoder

from app.server.database.schedule import (
    make_daily_schedule,
    delete_user_schedule_data
)

router = APIRouter()

@router.post('/{user_id}/{roster_id}/{roster_group_id}/{date}/{prev_date}')
async def append_daily_schedule(user_id: str, roster_id: str, roster_group_id: str, date: str, prev_date: str):
    result = await make_daily_schedule(user_id, roster_id, roster_group_id, date, prev_date)
    return result

@router.put('/clean_user_schedule')
async def delete_user_schedule_field():
    result = await delete_user_schedule_data()
    if result:
        return "All users schedule field has successfully deleted"
    else:
        return "Error..."