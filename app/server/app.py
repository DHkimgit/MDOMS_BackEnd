from fastapi import FastAPI

from app.server.routes.user import router as UserRouter

app = FastAPI()

app.include_router(UserRouter, tags=["User"], prefix="/user")

# python app/main.py
# https://testdriven.io/blog/fastapi-mongo/
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}