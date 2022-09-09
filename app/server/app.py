from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.server.routes.user import router as UserRouter
from app.server.routes.roster import router as RosterRouter
from app.server.routes.login import router as LoginRouter
from app.server.routes.logictest import router as LogicTestRouter
from app.server.routes.roster_information import router as RosterInformationRouter
app = FastAPI()

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(RosterRouter, tags=["Roster"], prefix="/roster")
app.include_router(RosterInformationRouter, tags=["RosterInformation"])
app.include_router(LoginRouter, tags=["Login"], prefix="/auth")
app.include_router(LogicTestRouter, tags=["Test"], prefix="/test")

# python app/main.py
# https://testdriven.io/blog/fastapi-mongo/
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}