from fastapi import FastAPI, status, HTTPException, Depends, APIRouter, Body
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from fastapi.encoders import jsonable_encoder
from datetime import date, datetime, timezone, timedelta
from app.server.database.user import (
    get_current_active_user_servicenumber
)
from app.server.database.forum import (
    fine_writer_name,
    append_post,
    get_post
)
from app.server.models.forum import (
    FourmSchema,
    CommentSchema
)

router = APIRouter()

@router.post('/')
async def registering_a_post(post_body: FourmSchema = Body(...), servicenumber: str = Depends(get_current_active_user_servicenumber)):
    appended_data = jsonable_encoder(post_body)
    name = await fine_writer_name(servicenumber)
    appended_data["writer_name"] = name
    appended_data["writer_service_numer"] = servicenumber
    KST = timezone(timedelta(hours=9))
    time_record = datetime.now(KST)
    _day = str(time_record)[:10]
    _time = str(time_record.time())[:8]
    appended_data["write_date"] = _day
    appended_data["write_time"] = _time
    print(appended_data)
    append_data = await append_post(appended_data)
    if append_data:
        result = await get_post(servicenumber, appended_data["write_date"], appended_data["write_time"], appended_data["category"])
        return result
    else:
        return "error"