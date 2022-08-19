from fastapi import FastAPI

from app.server.routes.user import router as UserRouter
from app.server.routes.roster import router as RosterRouter
from app.server.routes.login import router as LoginRouter
app = FastAPI()

app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(RosterRouter, tags=["Roster"], prefix="/roster")
app.include_router(LoginRouter, tags=["Login"], prefix="/auth")

# python app/main.py
# https://testdriven.io/blog/fastapi-mongo/
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}