from fastapi import FastAPI, status, HTTPException, Depends, APIRouter, Body
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from fastapi.encoders import jsonable_encoder
from app.server.database.unit import (
    get_all_units,
    add_unit,
    delete_unit,
    check_root_permission,
    debug_test
)
from app.server.database.user import (
    get_current_active_user_servicenumber
)
from app.server.models.unit import (
    UnitSchema
)
router = APIRouter()

# Return Evert Unit
@router.get("/", response_description="Units retrieved")
async def get_all_unit():
    result = await get_all_units()
    return result

@router.post("/", response_description="Unit data successfully added to database")
async def post_unit_data(unit_data: UnitSchema = Body(...), servicenumber: str = Depends(get_current_active_user_servicenumber)):
    added_data = jsonable_encoder(unit_data)
    check_permission = await check_root_permission(servicenumber)
    if check_permission == False:
        return "Permission Error: This account has low level permission"
    else:
        result = await add_unit(added_data)
        return result

@router.delete("/{id}", response_description="User data deleted from the database")
async def delete_unit_data(id: str, servicenumber: str = Depends(get_current_active_user_servicenumber)):
    check_permission = await check_root_permission(servicenumber)
    print(check_permission)
    if check_permission == False:
        return "Permission Error: This account has low level permission"
    else:
        result = await delete_unit(id)
        if result:
            return f"unit id {id} deleted"
        else:
            return "Error"