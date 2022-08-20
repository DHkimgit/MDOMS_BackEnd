from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.server.routes.user import router as UserRouter
from app.server.routes.roster import router as RosterRouter
from app.server.routes.login import router as LoginRouter
app = FastAPI()

origins = [
    "https://mdoms-front.run.goorm.io",
    "https://mdoms-backend.run.goorm.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(RosterRouter, tags=["Roster"], prefix="/roster")
app.include_router(LoginRouter, tags=["Login"], prefix="/auth")

# python app/main.py
# https://testdriven.io/blog/fastapi-mongo/
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}