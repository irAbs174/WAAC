from fastapi import FastAPI
from pydantic import BaseModel
from db import DBUser

class UserRequest(BaseModel):
    name: str
    phone: str


app = FastAPI()

@app.post('/user/register')
async def user_login(user: UserRequest):
    db_user = DBUser()  # Create an instance of the DBUser class
    token = db_user.check_user_allowed(user.name, user.phone)
    return token

