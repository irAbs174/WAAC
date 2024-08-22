from fastapi import FastAPI
from pydantic import BaseModel
from db import DBUser

class UserRequest(BaseModel):
    name: str
    phone: str


app = FastAPI()

@app.post('/user/auth')
async def user_login(user: UserRequest):
    u = DBUser()
    u.check_user_table()
    token = u.auth(user.name, user.phone)
    return token

